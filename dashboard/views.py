from django.shortcuts import render
from .models import FoodConsumption
 
# Create your views here.
def dashboardPageView(request):
    data = FoodConsumption.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/dashboard.html', context)

