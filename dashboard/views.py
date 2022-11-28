from django.shortcuts import render

def dashboardPageView(request):
    context = {
 
    }
    return render(request, 'dashboard/dashboard.html', context)
# Create your views here.
