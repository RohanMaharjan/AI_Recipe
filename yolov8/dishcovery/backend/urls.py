from django.urls import path
from .views import DetectFoodAPIView

urlpatterns = [
    path('detect-food/', DetectFoodAPIView.as_view()),
]
