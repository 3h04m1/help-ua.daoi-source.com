from django.urls import path, include
from .views import index, mapview

urlpatterns = [
    path("", index, name="index" ),
    path("map/", mapview, name="map"),
]
