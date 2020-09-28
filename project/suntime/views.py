from django.db.models import Q
from django.shortcuts import render

# Create your views here.

import logging

from django.utils.html import escape

logger = logging.getLogger("Views")

from django.http import JsonResponse


from . import helper

def get_sunrise_sunset(request):
    date = request.GET.get('date', None)
    country_name = request.GET.get('country_name', None)
    if not date:
        raise ValueError("Date is not supplied")
    if not country_name:
        raise ValueError("Country is not supplied")
    country_name = country_name.strip("”").strip()
    lat, lng = helper.get_lat_lng_from_country_name(country_name)
    sunrise, sunset = helper.get_sun_times(date, lat, lng)
    response_data = {
        'sunrise': sunrise,
        'sunset': sunset
    }
    return JsonResponse(response_data, status=202)

def vue_suntime(request):
    country_names = helper.get_country_names()
    context = {
        'country_names': country_names
    }
    return render(request, 'VueSuntime.html', context)

def index(request):
    country_names = helper.get_country_names()
    context = {
        'country_names': country_names
    }
    return render(request, 'suntime.html', context)

