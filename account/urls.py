from django.urls import path
from .views import (
    UserLogoutView,
    UserRegisterView,
    user_login
)

urlpatterns = [
    # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
