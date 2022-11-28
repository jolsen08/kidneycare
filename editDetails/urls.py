from django.urls import path
from .views import dashboardPageView

urlpatterns = [ 
    path("", dashboardPageView, name="dashboard"), 
]  