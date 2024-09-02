from django.urls import path
from .views import (
    UserLogoutView,
    UserRegisterView,
    login
)

urlpatterns = [
    # Authentication URLs
    path('login/', login, name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
