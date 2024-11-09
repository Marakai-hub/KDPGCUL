from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This is necessary to access the Django admin page
    # Your other URL patterns...
    path('', include('farmers.urls')),
    # Other patterns...
]
