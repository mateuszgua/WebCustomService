import csv

from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
from django.contrib.auth.models import User

def upload_file_view(requsest):
    form = CsvModelForm(requsest.POST or None, requsest.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0 or row == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    user = User.objects.get(username=row[1])
                    print(row)
                    print(type(row))
            obj.activated = True
            obj.save()
    return render(requsest,
                  'csvs/upload.html',
                  {'form': form})

