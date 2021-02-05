from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.db.models import Q

import json
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from rest_auth.views import LoginView

from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .serializers import RegistrationSerializer, UserProfileSerializer, UserProfileUpdateSerializer, DeleteProfileSerializer, CustomLoginSerializer, TokenSerializer

# from generics.filters import reduce_comma
from itertools import chain
from django.conf import settings
from django.shortcuts import render_to_response
from rest_framework.decorators import api_view

User = get_user_model()


class RegistrationView(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        # token, created = Token.objects.get_or_create(user=user)
        # data = serializer.data
        data={}
        data["msg"] = 'User Registration Successful'

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginAPIView(GenericAPIView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            print(user)
            token, _ = Token.objects.get_or_create(user=serializer.validated_data['user'])
            data=TokenSerializer(token).data
            profile={}
            profile['role']='general'
            profile['user_id']= serializer.validated_data['user'].pk
            profile['first_name']=serializer.validated_data['user'].first_name
            profile['email']=serializer.validated_data['user'].email
            data['profile']=profile
            data['status']=status.HTTP_200_OK
            return Response(
                data,
                status=status.HTTP_200_OK,
            )
        else:
            error={
             status:500,
             error:"Username Or Password is invalid"
            }
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class ActivateViews(APIView):
    queryset = User.objects.all()

    def get(self, request, pk, format='json'):
        """
		receives the validation key, checks if it exists.

		If it does, return succes message
		Else return error (invalid validation key or expired key)

        """
        return_message = ''

        # use pk to validate the user
        found_users = self.queryset.filter(activation_key=pk)

        if len(found_users) == 0:
        	return_message = 'Invalid activation key'

        elif len(found_users) > 1:
        	return_message = 'Multiple users with this activation key'
        else:
        	user = found_users[0]
        	user.is_active = True
        	user.activation_key = ''
        	user.save()
        	return_message = 'Account activated'

		# give response
        content = {'message': return_message}
        return Response(content)


class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UpdateProfileView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        try:
            if self.request.data['id'] and (self.request.user.type == 'admin' or
                                         self.request.user.is_superuser):
                return User.objects.get(pk=self.request.data['id'])
        except MultiValueDictKeyError:
            pass
        return self.request.user


class DeleteProfileView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DeleteProfileSerializer

    def get_object(self, queryset=None):
        try:
            pk = self.kwargs['pk']
            if self.request.user.type == 'admin' or self.request.user.is_superuser:
                user = User.objects.get(pk=pk)
                if user:
                    current_prof_pic = User.objects.get(pk=user.id).profile_pic
                    if not current_prof_pic.url.endswith('profile_pictures/default_pic.png'):
                        default_storage.delete(current_prof_pic)
                return user
        except KeyError:
            user = self.request.user
            if user:
                current_prof_pic = User.objects.get(pk=user.id).profile_pic
                if not current_prof_pic.url.endswith('profile_pictures/default_pic.png'):
                    default_storage.delete(current_prof_pic)
            return user


class GetUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        try:
            if self.request.query_params['exclude_me']:
                me_flag = True
            else:
                me_flag = False
        except Exception:
            me_flag = False
        queryset = []
        types = self.request.query_params.get('type', None)
        search = self.request.query_params.get('search', '')
        sort = self.request.query_params.get('sort', 'first_name')
        if self.request.user.type == 'admin' or self.request.user.type == 'auteur' or self.request.user.is_superuser: #or self.request.user.is_admin:
            if types:
                value = types.split(',')
                typesArr = reduce(reduce_comma, value, [])
            else:
                if me_flag:
                    queryset = User.objects.exclude(pk=self.request.user.id).order_by(sort)
                else:
                    queryset = User.objects.all().order_by(sort)
            return queryset
        else:
            return User.objects.none()


@api_view(['POST'])
def resend_activation_link(request):
    params = json.loads(request.body)
    email = params['email']
    try:
        user = User.objects.get(email=email)
        if not user.is_active:
            email_subject = "RI Studio %s: activeer je email binnen 2 dagen" % (settings.RIS_MUNICIPALITY)
            context = {
                'username': user.username,
                'portal_url': settings.FRONTEND_URL,
                'municipality': settings.RIS_MUNICIPALITY,
                'link': "%sactiveer-account/%s" % (settings.FRONTEND_URL, user.activation_key),
                'bcolor': settings.COLOR[settings.RIS_MUNICIPALITY]
            }
            html_content = render_to_response('activation_email.html', context)
            mail = MailGun()
            mail.send_mail(email, email_subject, False, html_content)
            return JsonResponse({'response': 'Activation email sent'})
        else:
            return JsonResponse({'response': 'Already activated'})
    except Exception:
        return JsonResponse({'response': 'Geen account met deze e-mail gevonden'})


def test_template(request):
    context = {
        'username': 'username',
        'password': False,
        'portal_url': settings.FRONTEND_URL,
        'municipality': settings.RIS_MUNICIPALITY,
        'link': "%sactiveer-account" % (settings.FRONTEND_URL),
        'bcolor': settings.COLOR[settings.RIS_MUNICIPALITY],
        'uid': 'uid',
        'token': 'token',
        'item': {
            'name': 'Name',
            'date': '2016-12-28T17:54:38',
            'last_modified': '2016-12-28T17:54:38'
        },
        'type': 'document',
        'url': 'url'
    }
    return render_to_response('password_reset_email.html', context)
