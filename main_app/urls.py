from django.contrib import admin
from django.urls import path, include
from .views import newsCreate, NewsListAPIview

urlpatterns = [
    path("", newsCreate, name="Create News"),
    path("news/", NewsListAPIview.as_view(), name="News List"),
]
