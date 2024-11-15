from django.urls import path
from . import views

urlpatterns = [
    path("january", views.January),
    path("feburary", views.feburary)
]
