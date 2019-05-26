from django.views import View
from django.shortcuts import render

from weather_tracker.contrib.forms import WeatherFinderForm
from weather_tracker.contrib.utils import GoogleGeocode, DarkSky
from weather_tracker.contrib.models import WeatherUsage


class HomePageView(View):
    template_name = "pages/home.html"
    form_class = WeatherFinderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            formatted_address, lng, lat = GoogleGeocode(cleaned_data.get('location')).get_location()
            temperature = DarkSky(lat=lat, lng=lng).get_temperature()
            ip = self._get_client_ip(request)
            search = self._register_search(ip, formatted_address, lat, lng, temperature)

            return render(request, self.template_name, {'form': form, 'formatted_address': formatted_address,
                                                        'temperature': temperature, 'search': search})

        return render(request, self.template_name, {'form': form})

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    @staticmethod
    def _register_search(ip, location, lat, lng, temperature):
        search = WeatherUsage(**locals())
        search.save()
        return search
