from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Device, Content
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import DeviceProfileFormSet
from django.forms.models import modelform_factory
from django.apps import apps


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

class DeviceCreateView(OwnerDeviceEditMixin,
                       CreateView):
    permission_required = 'devicedata.add_device'

class DeviceUpdateView(OwnerDeviceEditMixin,
                       UpdateView):
    template_name = 'devicedata/manage/device/form.html'
    permission_required = 'devicedata.change_device'

class DeviceDeleteView(OwnerDeviceMixin,
                       DeleteView):
    template_name = 'devicedata/manage/device/delete.html'
    success_url = reverse_lazy('manage_device_list')
    permission_required = 'devicedata.delete_device'

class DeviceDeviceProfileUpdateView(TemplateResponseMixin, View):
    template_name = 'devicedata/manage/deviceprofile/formset.html'
    device = None

    def get_formset(self, data=None):
        return DeviceProfileFormSet(instance=self.device,
                                    data=data)

    def dispatch(self, request, pk):
        self.device = get_object_or_404(Device,
                                        id=pk,
                                        owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'device': self.device,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_device_list')
        return self.render_to_response({'device': self.device,
                                        'formset': formset})

class ContentCreateUpdateView(TemplateResponseMixin, View):
    deviceprofile = None
    model = None
    obj = None
    template_name = 'devicedata/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['file']:
            return apps.get_model(app_label='devicedata',
                                  model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'order',
                                                 'created',
                                                 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, deviceprofile_id, model_name, id=None):
        self.deviceprofile = get_object_or_404(Device,
                                        id=deviceprofile_id,
                                        device__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner=request.user)
        return super(ContentCreateUpdateView,
                     self).dispatch(request, deviceprofile_id, model_name, id)

    def get(self, request, deviceprofile_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

    def post(self, request, deviceprofile_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance=self.obj,
                             data=request.POST,
                             files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                #New content
                Content.objects.create(deviceprofile=self.deviceprofile,
                                       item=obj)
            return redirect('deviceprofile_content_list', self.deviceprofile.id)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

class ContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(Content,
                                    id=id,
                                    deviceprofile__device__owner=request.user)
        deviceprofile = content.deviceprofile
        content.item.delete()
        content.delete()
        return redirect('deviceprofile_content_list', deviceprofile.id)


