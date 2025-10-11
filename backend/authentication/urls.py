from django.urls import path
from .views import (
    LoginView,
    RegistrationView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='Login'),
    path('register/', RegistrationView.as_view(), name='Register')
]
