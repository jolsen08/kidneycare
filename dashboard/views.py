from django.shortcuts import render
from .models import Food
 
# Create your views here.
def dashboardPageView(request):
    data = Food.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'dashboard/dashboard.html', context)

