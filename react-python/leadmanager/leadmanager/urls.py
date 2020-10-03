from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('', include('frontend.urls')), #  home page react
   path('', include('leads.urls')) # home page api
]
