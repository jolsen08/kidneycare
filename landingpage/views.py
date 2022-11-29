from django.shortcuts import render

def indexPageView(request):
    context = {
 
    }
    return render(request, 'landingpage/index.html', context)

def HomePageView(request):
    context = {
 
    }
    return render(request, 'accounts/home.html', context)

