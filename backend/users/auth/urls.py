from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views.login import CustomLoginView as LoginView
from .views.logout import LogoutView
from .views.me import MeView
from .views.register import UserRegisterView
from .views.change_password import ChangePasswordView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]

__all__ = ['urlpatterns']
