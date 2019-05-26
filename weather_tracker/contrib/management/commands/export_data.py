import os
import json

from django.conf import settings
from django.db.models import Count
from django.core.management.base import BaseCommand

from weather_tracker.contrib.models import WeatherUsage


class Command(BaseCommand):
    help = 'Create file with usage service by IP for each day.'

    def handle(self, *args, **kwargs):
        self.data = self._mount_data()
        self.formatted_data = self._format_data()
        self._create_file()
        self.stdout.write(self.style.SUCCESS('File create to successfully'))

    def _mount_data(self):
        return WeatherUsage.objects.values('created_at', 'ip').annotate(Count('ip'))

    def _format_data(self):
        formatted = {}

        for item in self.data:
            created_at = item.get('created_at').strftime("%Y-%m-%d")
            if not hasattr(formatted, created_at):
                formatted[created_at] = []
            formatted[created_at].append({'IP': item.get('ip'), 'COUNT': item.get('ip__count')})

        return formatted

    def _create_file(self):
        directory = settings.EXPORT_PATH
        file_path = '{}exported.json'.format(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, 'w') as f:
            f.write(json.dumps(self.formatted_data, indent=4, sort_keys=True))
