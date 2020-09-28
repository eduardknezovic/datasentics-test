
from django.urls import path
from .views import index, get_sunrise_sunset, vue_suntime

urlpatterns = [
    path("", index, name="suntime-index"),
    path("get_sunrise_sunset", get_sunrise_sunset, name="get_sunrise_sunset"),
    path("vue_suntime", vue_suntime, name="vue_suntime"),
]