from django.urls import path
from .views import dashboardPageView, dailyBars

urlpatterns = [ 
    path("", dashboardPageView, name="dashboard"), 
    path("dailybars/", dailyBars, name="dailybars"), 

]  