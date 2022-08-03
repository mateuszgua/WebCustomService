from django.urls import path
from . import views

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
    path('<pk>/deviceprofile/',
         views.DeviceDeviceProfileUpdateView.as_view(),
         name='device_deviceprofile_update'),
    path('deviceprofile/<int:deviceprofile_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(),
         name='deviceprofile_content_create'),
    path('deviceprofile/<int:deviceprofile_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(),
         name='deviceprofile_content_update'),
    path('content/<int:id>/delete/',
         views.ContentDeleteView.as_view(),
         name='deviceprofile_content_delete'),
    path('deviceprofile/<int:deviceprofile_id>/',
         views.DeviceProfileListView.as_view(),
         name='deviceprofile_content_list'),

]