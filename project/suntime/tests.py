from django.test import TestCase

# Create your tests here.
import pytest
import suntime.helper as helper

import requests

def test_basic():
    assert True

@pytest.mark.xfail
def test_NAME():
    assert False

def test_get_sun_times():
    lat="36.7201600"
    lng="-4.4203400"
    date="2020-12-03"
    sunrise, sunset = helper.get_sun_times(date, lat, lng)
    assert sunrise == "7:14"
    assert sunset == "5:01"

