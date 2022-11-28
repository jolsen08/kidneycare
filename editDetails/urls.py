from django.urls import path
from .views import editDetailsPageView

urlpatterns = [ 
    path("", editDetailsPageView, name="editdetails"), 
]  