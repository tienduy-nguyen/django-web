from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('@<str:user_slug>/', views.profile, name='profile'),
    path('profile/edit/', views.editProfile, name='editProfile'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name="users/passwordReset.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/passwordResetDone.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/passwordResetConfirm.html"),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/passwordResetComplete.html"),
         name='password_reset_complete'),

]
