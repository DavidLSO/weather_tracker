from django.db.models import Model, GenericIPAddressField, CharField, DecimalField, DateField
from django.utils.translation import gettext as _


class WeatherUsage(Model):
    ip = GenericIPAddressField()
    location = CharField(max_length=255)
    lat = CharField(max_length=50)
    lng = CharField(max_length=50)
    temperature = DecimalField(decimal_places=3, max_digits=5)
    created_at = DateField(auto_now=True)

    class Meta:
        verbose_name = _("Weather Usage")
        verbose_name_plural = _("Weather Usages")

    def __str__(self):
        return 'Temperature at {} is {} <b>C˚</b>.'.format(self.location.title(), self.temperature)
