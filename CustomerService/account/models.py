from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_city = models.CharField(max_length=200)
    company_street = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'User profile {}.'.format(self.user.username)