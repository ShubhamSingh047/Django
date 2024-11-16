from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month_num>", views.montly_challenge_num),
    path("<str:month>", views.montly_challenge, name='month_challenge'),
]
