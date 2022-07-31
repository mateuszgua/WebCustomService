from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Device
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)

class OwnerDeviceMixin(OwnerMixin,
                       LoginRequiredMixin,
                       PermissionRequiredMixin):
    model = Device
    fields = ['title', 'slug', 'overview']
    success_url = reverse_lazy('manage_device_list')

class OwnerDeviceEditMixin(OwnerDeviceMixin, OwnerEditMixin):
    fields = ['title', 'slug', 'overview']
    success_url = reverse_lazy('manage_device_list')
    template_name = 'devicedata/manage/device/form.html'

class ManageDeviceListView(OwnerDeviceMixin, ListView):
    template_name = 'devicedata/manage/device/list.html'
    permission_required = 'devicedata.view_device'

class DeviceCreateView(PermissionRequiredMixin,
                       OwnerDeviceEditMixin,
                       CreateView):
    permission_required = 'devicedata.add_device'

class DeviceUpdateView(PermissionRequiredMixin,
                       OwnerDeviceEditMixin,
                       UpdateView):
    template_name = 'devicedata/manage/device/form.html'
    permission_required = 'devicedata.change_device'

class DeviceDeleteView(PermissionRequiredMixin,
                       OwnerDeviceMixin,
                       DeleteView):
    template_name = 'devicedata/manage/device/delete.html'
    success_url = reverse_lazy('manage_device_list')
    permission_required = 'devicedata.delete_device'
