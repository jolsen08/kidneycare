from django.shortcuts import render

def dashboardPageView(request):
    context = {
 
    }
    return render(request, 'dashboard/index.html', context)
# Create your views here.
