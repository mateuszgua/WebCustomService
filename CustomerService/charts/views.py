from django.shortcuts import render

import pandas as pd
from .models import FileName
#from devicedata.models import ItemBase

def index(request):

    #files = ItemBase.objects.all()
    files = FileName.objects.all()

    if request.method == 'POST':
        attributeid = request.POST.get('attributeid')

    return render(request,
                  'charts/results.html',
                  {'files': files})


def readfile(filename):
    global rows, columns, data, my_file, missing_values
    my_file = pd.read_csv(filename, sep='[:;,|_]', engine='python')
    data = pd.DataFrame(data=my_file, index=None)
    print(data)

    #rows and columns
    rows = len(data.axes[0])
    columns = len(data.axes[1])

    #find missing data
    missingsings = ['?', '--']
    null_data = data[data.isnull().any(axis=1)]
    missing_values = len(null_data)

def results(request):
    return render(request,
                  'charts/results.html',
                  {'section': 'results'})