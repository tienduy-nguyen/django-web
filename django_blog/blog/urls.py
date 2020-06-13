from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<str:slug>/', views.postDetail, name='postDetail'),
    path('category/', views.categoryList, name='categoryList'),
    path('category/<str:slug>/',
         views.categoryDetail, name='categoryDetail'),
]
