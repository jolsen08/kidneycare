from django.urls import path
from .views import indexPageView, HomePageView


urlpatterns = [ 
    path("landingpage/", indexPageView, name="index"), 
    path("", HomePageView, name="homepage")
]   
