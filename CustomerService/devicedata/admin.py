from django.contrib import admin
from .models import Device, DeviceProfile

class DeviceProfileInline(admin.StackedInline):
    model = DeviceProfile

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [DeviceProfileInline]




