from django import forms
from django.forms.models import inlineformset_factory
from .models import Device, DeviceProfile

DeviceProfileFormSet = inlineformset_factory(Device,
                                             DeviceProfile,
                                             fields=['title', 'description'],
                                             extra=2,
                                             can_delete=True)