from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('@<str:user_slug>/', views.profile, name='profile'),
    path('profile/edit/', views.editProfile, name='editProfile'),
    path('logout/', views.logout, name='logout')
]
