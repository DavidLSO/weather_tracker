import json
import requests

from django.conf import settings


class GoogleGeocode:
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"
    parameter = None

    def __init__(self, parameter):
        self.parameter = self._format_parameter(parameter)

    @staticmethod
    def _format_parameter(parameter):
        formated = parameter
        if formated:
            formated = formated.replace('-', '')
            if formated.isdigit():
                formated = '{}-{}'.format(formated[:-3], formated[-3:])
        return formated

    def get_location(self):
        try:
            r = requests.get(self.base_url.format(self.parameter, settings.GOOGLE_API_KEY))
            formatted_address = ''
            lat = ''
            lng = ''

            if r.status_code == 200:
                payload = json.loads(r.text)
                formatted_address = payload['results'][0]['formatted_address']
                lat = payload['results'][0]['geometry']['location']['lat']
                lng = payload['results'][0]['geometry']['location']['lng']

            return formatted_address, lng, lat
        except Exception as e:
            raise Exception(e)


class DarkSky:
    base_url = "https://api.darksky.net/forecast/{}/{},{}?units=si"
    parameter = None

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def get_temperature(self):
        try:
            r = requests.get(self.base_url.format(settings.DARK_SKY_API_KEY, self.lat, self.lng))
            temperature = None

            if r.status_code == 200:
                payload = json.loads(r.text)
                temperature = payload['hourly']['data'][0]['temperature']

            return temperature
        except Exception as e:
            raise Exception(e)
