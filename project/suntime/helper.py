
import logging
import requests

from .models import Country

logger = logging.getLogger("Suntimes Helper")

def get_country_names():
    countries = Country.objects.order_by('name').all()
    country_names = [country.name for country in countries]
    return country_names

def get_lat_lng_from_country_name(country_name):
    country_name = country_name.strip("”").strip()
    logger.error(country_name)
    country = Country.objects.get(name=country_name)
    return country.lat, country.long

def get_sun_times(date, lat, lng):
    url = "https://api.sunrise-sunset.org/json/"
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}")
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise = format_time_result(sunrise)
    sunset = format_time_result(sunset)
    return sunrise, sunset

def format_time_result(time):
    hours, minutes = time.split(":")[:2]
    if "PM" in time:
        hours = str((int(hours) + 12)% 24)
    return ":".join([hours, minutes])

