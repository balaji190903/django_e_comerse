from django.urls import path
from .views import CartListCreateView, CartDetailView

urlpatterns = [
    path('', CartListCreateView.as_view()),
    path('<int:pk>/', CartDetailView.as_view()),
]
