from django.urls import path
from .views.logout import LogoutView
from .views.me import MeView
from .views.register import UserRegisterView


urlpatterns = [    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

__all__ = ['urlpatterns']
