
from django.urls import path
from .views import index, get_sunrise_sunset

urlpatterns = [
    path("", index, name="suntime"),
    path("get_sunrise_sunset", get_sunrise_sunset, name="get_sunrise_sunset"),
]