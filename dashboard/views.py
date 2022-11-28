from django.shortcuts import render

def dashboardPageView(request):
    context = {
 
    }
    return render(request, 'base.html', context)
# Create your views here.
