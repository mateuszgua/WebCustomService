import csv

from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
from django.shortcuts import get_object_or_404

def upload_file_view(request, *args, **kwargs):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        #obj = Csv.objects.filter(activated=False)
        #obj = get_object_or_404(Csv, activated=False)
        obj = get_object_or_404(Csv, pk=kwargs['pk'])
        with open(obj.file_name.path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                Csv.objects.get_or_create(
                    id_data=row[0],
                    profile=row[1],
                )

    return render(request,
                  'csvs/upload.html',
                  {'form': form})

""" if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.filter(activated=False)
        with open(obj.file_name.path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    #row = row.split()
                    id_data = int(row[0])
                    profile = row[1]
                    print(row)
                    Csv.objects.create(
                        id_data=id_data,
                        profile=profile,
                    )
            obj.activated = True
            obj.save()

    return render(request,
                  'csvs/upload.html',
                  {'form': form})

"""
