from django.urls import path
from .views import SignupView, LoginView, AdminLoginView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('admin/login/', AdminLoginView.as_view()),
]
