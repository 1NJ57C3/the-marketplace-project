from django.urls import path
from .views import LogoutView, MeView, UserRegisterView

urlpatterns = [    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

__all__ = ['urlpatterns']
