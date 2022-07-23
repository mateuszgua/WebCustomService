from django.db import models
from django.contrib.auth.models import User

class MeasData(models.Model):
    index = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.CharField(max_length=100)
    date_meas = models.DateTimeField()
    time_meas = models.DateTimeField()
    humidity = models.PositiveIntegerField()
    temp_cel = models.PositiveIntegerField()
    temp_fahr = models.PositiveIntegerField()
    class_ISO4 = models.PositiveIntegerField()
    class_ISO6 = models.PositiveIntegerField()
    class_ISO14 = models.PositiveIntegerField()
    class_NAS = models.PositiveIntegerField()
    class_GOST = models.PositiveIntegerField()
    class_SAE4 = models.PositiveIntegerField()
    class_SAE6 = models.PositiveIntegerField()
    class_SAE14 = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'MeasData {}'.format(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)