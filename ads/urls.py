from django.urls import path, include
from .views import PostListView
from . import views

urlpatterns = [
    path('', views.index, name='ads-index'),
    path('about/', views.about, name='ads-about'),
    path('ads/', PostListView.as_view(), name='ads-list')
]