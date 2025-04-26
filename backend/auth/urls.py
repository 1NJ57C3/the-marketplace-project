from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from auth.views.change_password import ChangePasswordView
from auth.views.login import CustomLoginView as LoginView
from auth.views.logout import LogoutView
from auth.views.register import UserRegisterView
from auth.views.password_reset_request import CustomPasswordResetRequestView as PasswordResetRequestView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
]

__all__ = ['urlpatterns']
