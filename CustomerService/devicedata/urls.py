from django.urls import path
from . import views

app_name = 'devicedata'

urlpatterns = [
    path('mine/',
         views.ManageDeviceListView.as_view(),
         name='manage_device_list'),
    path('create/',
         views.DeviceCreateView.as_view(),
         name='device_create'),
    path('<pk>/edit/',
         views.DeviceUpdateView.as_view(),
         name='device_edit'),
    path('<pk>/delete/',
         views.DeviceDeleteView.as_view(),
         name='device_delete'),
]