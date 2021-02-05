from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth import views as rest_auth_views
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views as local_views


urlpatterns = [
    path('accounts/password/reset', rest_auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/confirm/<uidb64>-<token>)', rest_auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

	# Local views
    path('accounts/profile', local_views.UserProfileView.as_view(), name='user_profile'),
    path('accounts/profile/change', local_views.UpdateProfileView.as_view(), name='change_user_profile'),
    path('accounts/profile/delete', local_views.DeleteProfileView.as_view(), name='delete_profile'),
    path('accounts/profile/delete/<pk>)', local_views.DeleteProfileView.as_view(), name='delete_profile'),
    path('accounts/register', local_views.RegistrationView.as_view(), name='register'),
    re_path(r'^accounts/activate/(?P<pk>[^/]+)', local_views.ActivateViews.as_view(), name='activate'),
    path('accounts/resend-activation-link', local_views.resend_activation_link, name='resend_activation_link'),

    # Django Rest Auth
    # path('accounts/login-token/', obtain_jwt_token, name='login-token'),
    # path('accounts/login-token-refresh/', refresh_jwt_token, name='login-token-refresh'),
    # path('accounts/login--token-verify/', verify_jwt_token, name='login-token-verify'),
    path('accounts/login', local_views.UserLoginAPIView.as_view(), name='rest_login'),
    path('accounts/logout', rest_auth_views.LogoutView.as_view(), name='rest_logout'),
    path('accounts/user', local_views.UserProfileView.as_view(), name='user_details'),
    path('accounts/password/change', rest_auth_views.PasswordChangeView.as_view(), name='rest_password_change'),

    path('accounts/users', local_views.GetUsersView.as_view(), name='get_users'),
    # url(r'^accounts/user_items/$', local_views.GetUserItemCounts.as_view({'get': 'list'}), name='get_user_items'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
