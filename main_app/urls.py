from django.contrib import admin
from django.urls import path, include
from .views import newsCreate

urlpatterns = [
    path("", newsCreate, name="Create News"),
]
