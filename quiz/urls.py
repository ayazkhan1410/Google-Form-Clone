from django.urls import path, include
from .views import *

urlpatterns = [
    path("choices/", ChoiceAPIView.as_view())
]
