from django.urls import path
from .views import LogoutView, UserRegisterView

urlpatterns = [    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

__all__ = ['urlpatterns']
