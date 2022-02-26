from django.urls import path, include
from .views import index, mapview,betamap, need_help, help, help_list, need_help_list

urlpatterns = [
    path("", index, name="index" ),
    path("map/", mapview, name="map"),
    path("help/", help, name="help" ),
    path("need_help/", need_help, name="need_help" ),
    path("help_list/", help_list, name="help_list" ),
    path("need_help_list/", need_help_list, name="need_help_list" ),
    path("betamap/", betamap, name="betamap"),
]
