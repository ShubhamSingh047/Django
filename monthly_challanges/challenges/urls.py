from django.urls import path
from . import views

urlpatterns = [
    path("<str:month>", views.montly_challenge),
]
