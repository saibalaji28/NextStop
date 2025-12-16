from django.urls import path
from .views import route_view, map_view

urlpatterns = [
    path("route/", route_view, name="route"),
    path("map/", map_view, name="map"),
]