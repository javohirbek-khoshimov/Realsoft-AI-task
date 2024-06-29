# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include users app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in authentication URLs
    path('accounts/', include('allauth.urls')),  # Include django-allauth URLs
]

