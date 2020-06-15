from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('<str:slug>/', PostDetailView.as_view(), name='postDetail'),
    path('post/new/', PostCreateView.as_view(), name='postCreate'),
    path('category/', views.categoryList, name='categoryList'),
    path('category/<str:slug>/',
         views.categoryDetail, name='categoryDetail'),
]
