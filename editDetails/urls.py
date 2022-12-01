from django.urls import path
from .views import editDetailsPageView
from .views import searchfood

urlpatterns = [ 

    path("searchfood", searchfood, name="searchfood"),
    path("", editDetailsPageView, name="editdetails"),

]  