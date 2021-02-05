from django.shortcuts import render


from dataAPI import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from dataAPI.models import HouseholdQuestions, PersonalQuestions, HouseholdData, AttributeLookup, HouseholdQuestionaireMatch, PersonalQuestionaireMatch, PersonalData

from django.db.models import Sum, Count
from django.db.models import F
from rest_framework import status

household_variables_match = HouseholdQuestionaireMatch.objects.all()
household_variables_column_match ={

}
for vm in household_variables_match:
    household_variables_column_match[vm.small]=vm.original

personal_variables_match = PersonalQuestionaireMatch.objects.all()
personal_variables_column_match ={

}
for vm in personal_variables_match:
    personal_variables_column_match[vm.small]=vm.original
# Create your views here.
class householdQuestionsList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self):
        try:
            # print(adminid)
            return HouseholdQuestions.objects.filter(odk_data_type='select_one')
        except HouseholdQuestions.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        data = self.get_object()
        # print(data)
        serializer = serializers.houseHoldQuestionsSerializer(data, many=True)
        return Response(serializer.data)

class householdQueryDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, ward, variable):
        try:
            # print(adminid)
            if ward == 0:
                data = HouseholdData.objects.all().values(category=F(variable)).annotate(value = Count(variable))
            else:
                data = HouseholdData.objects.filter(ward=ward).values(category=F(variable)).annotate(value = Count(variable))
            # print(data)
            return data
        except HouseholdData.DoesNotExist:
            raise Http404
    def get(self, request, ward, variable, format=None):
        data = self.get_object(ward, variable)
        serializer = serializers.DataSerializer(data, many=True)
        # lookup data query
        lookup = HouseholdQuestions.objects.get(odk_question=household_variables_column_match[variable]).choice_list
        lookup_data = AttributeLookup.objects.filter(list_name=lookup)
        lookup_serializer = serializers.lookupSerializer(lookup_data, many=True)

        reponse_data = {
            'summary':serializer.data,
            'lookup': lookup_serializer.data
        }
        return Response(reponse_data, status=status.HTTP_200_OK)

class householdMicroDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, ward, variable, variableValue):
        try:
            # print(variableValue)
            # print({variable:variableValue})
            if ward == 0:
                data = HouseholdData.objects.filter(**{variable:variableValue})
            else:
                data = HouseholdData.objects.filter(ward=ward).filter(**{variable:variableValue})
            # print(data)
            return data
        except HouseholdData.DoesNotExist:
            raise Http404

    def get(self, request, ward, variable, variableValue, format=None):
        data = self.get_object(ward, variable, variableValue)
        # print(data)
        # questions=PersonalQuestions.objects.all()
        # # print(data)
        # tableHeader = serializers.personalQuestionsSerializer(questions, many=True)
        tableData = serializers.householdMicroDataSerializer(data, many=True)
        reponse_data = {
            # 'tableHeader':tableHeader.data,
            'tableData': tableData.data
        }
        return Response(reponse_data, status=status.HTTP_200_OK)


# Create your views here.
class personalQuestionsList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self):
        try:
            # print(adminid)
            return PersonalQuestions.objects.filter(odk_data_type='select_one')
        except PersonalQuestions.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        data = self.get_object()
        # print(data)
        serializer = serializers.personalQuestionsSerializer(data, many=True)
        return Response(serializer.data)

class personalQueryDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, ward, variable):
        try:
            # print(adminid)
            if ward == 0:
                data = PersonalData.objects.all().values(category=F(variable)).annotate(value = Count(variable))
            else:
                data = PersonalData.objects.filter(ward=ward).values(category=F(variable)).annotate(value = Count(variable))
            # print(data)
            return data
        except PersonalData.DoesNotExist:
            raise Http404
    def get(self, request, ward, variable, format=None):
        data = self.get_object(ward, variable)
        serializer = serializers.DataSerializer(data, many=True)
        # lookup data query
        lookup = PersonalQuestions.objects.get(odk_question=personal_variables_column_match[variable]).choice_list
        lookup_data = AttributeLookup.objects.filter(list_name=lookup)
        lookup_serializer = serializers.lookupSerializer(lookup_data, many=True)

        reponse_data = {
            'summary':serializer.data,
            'lookup': lookup_serializer.data
        }
        return Response(reponse_data, status=status.HTTP_200_OK)

class personalDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, format=None):
        data = PersonalData.objects.all()
        questions=PersonalQuestions.objects.all()
        # print(data)
        tableHeader = serializers.personalQuestionsSerializer(questions, many=True)
        tableData = serializers.personalDataSerializer(data, many=True)
        reponse_data = {
            'tableHeader':tableHeader.data,
            'tableData': tableData.data
        }
        return Response(reponse_data, status=status.HTTP_200_OK)

class personalMicroDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, ward, variable, variableValue):
        try:
            # print(variableValue)
            # print({variable:variableValue})
            if ward == 0:
                data = PersonalData.objects.filter(**{variable:variableValue})
            else:
                data = PersonalData.objects.filter(ward=ward).filter(**{variable:variableValue})
            # print(data)
            return data
        except PersonalData.DoesNotExist:
            raise Http404

    def get(self, request, ward, variable, variableValue, format=None):
        data = self.get_object(ward, variable, variableValue)
        # print(data)
        # questions=PersonalQuestions.objects.all()
        # # print(data)
        # tableHeader = serializers.personalQuestionsSerializer(questions, many=True)
        tableData = serializers.personalMicroDataSerializer(data, many=True)
        reponse_data = {
            # 'tableHeader':tableHeader.data,
            'tableData': tableData.data
        }
        return Response(reponse_data, status=status.HTTP_200_OK)

class dashboardDataList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request):
        stats={}
        stats['household'] = HouseholdData.objects.all().count()
        stats['male'] = PersonalData.objects.filter(q15=1).count()
        stats['female'] = PersonalData.objects.filter(q15=2).count()
        stats['allowance'] = PersonalData.objects.filter(q120=1).count()
        gender = PersonalData.objects.all().values(category=F('q15')).annotate(value = Count('q15'))
        literacy = PersonalData.objects.all().values(category=F('q22')).annotate(value = Count('q22'))

        serializer = serializers.DataSerializer(gender, many=True)
        # lookup data query
        lookup = PersonalQuestions.objects.get(odk_question=personal_variables_column_match['q15']).choice_list
        lookup_data = AttributeLookup.objects.filter(list_name=lookup)
        lookup_serializer = serializers.lookupSerializer(lookup_data, many=True)
        gender_data = {
            'summary':serializer.data,
            'lookup': lookup_serializer.data
        }
        stats['gender']=gender_data

        serializer = serializers.DataSerializer(literacy, many=True)
        # lookup data query
        lookup = PersonalQuestions.objects.get(odk_question=personal_variables_column_match['q22']).choice_list
        lookup_data = AttributeLookup.objects.filter(list_name=lookup)
        lookup_serializer = serializers.lookupSerializer(lookup_data, many=True)
        literacy_data = {
            'summary':serializer.data,
            'lookup': lookup_serializer.data
        }
        stats['literacy']=literacy_data

        reponse_data = {
            # 'tableHeader':tableHeader.data,
            # 'tableData': tableData.data
        }
        return Response(stats, status=status.HTTP_200_OK)



