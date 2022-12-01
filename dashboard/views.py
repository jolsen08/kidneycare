import json
from django.shortcuts import render
from .query import dict, list
import json
 
# Create your views here.
def dashboardPageView(request):
    data = dict
    context = {
        'data': data,
        'values': list
    }
    return render(request, 'dashboard/dashboard.html', context)
    print(data)

