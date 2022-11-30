from django.urls import path
from .views import trackerPageView
<<<<<<< HEAD
=======
# from .views import addUserFoodPageView
>>>>>>> a973b52a96a8b8b005ac86a405673315162dd21d

urlpatterns = [ 
    # path("adduserfood/<int:user_id>/", addUserFoodPageView, name="adduserfood"),
    path("", trackerPageView, name="tracker"), 
]   
