from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path("classify-number/", views.get_fact.as_view(), name="get view"),
]