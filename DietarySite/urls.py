from django.contrib import admin
from django.urls import path, include

# assigning urls routes for our other key pages
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('editdetails/', include('editDetails.urls')),
    path('tracker/', include('tracker.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('landingpage.urls')),
]
