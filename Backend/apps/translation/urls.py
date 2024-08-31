from django.urls import path
from .views import TranslateAPIView

app_name = "translation"

urlpatterns = [
    path('translate/', TranslateAPIView.as_view(), name='translate'),
]
