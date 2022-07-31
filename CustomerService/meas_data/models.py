from django.db import models
from django.utils.translation import gettext as _

class MeasData(models.Model):
    profile = models.CharField(_("profile"), max_length=100)
    date_meas = models.DateField(_("date"), auto_now=True)
    time_meas = models.TimeField(_("time"), auto_now=True)
    humidity = models.IntegerField(_("humidity"))
    temp_cel = models.IntegerField(_("temperature cel"))
    temp_fahr = models.IntegerField(_("temperature fahr"))
    class_ISO4 = models.IntegerField(_("ISO 4um"))
    class_ISO6 = models.IntegerField(_("ISO 6um"))
    class_ISO14 = models.IntegerField(_("ISO 14um"))
    class_NAS = models.IntegerField(_("NAS"))
    class_GOST = models.IntegerField(_("GOST"))
    class_SAE4 = models.IntegerField(_("SAE 4um"))
    class_SAE6 = models.IntegerField(_("SAE 4um"))
    class_SAE14 = models.IntegerField(_("SAE 4um"))
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'MeasData {}'.format(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)