
from django.contrib import admin
from django.urls import path
from . import views  # import view

urlpatterns = [
    path('admin/', admin.site.urls),
]
