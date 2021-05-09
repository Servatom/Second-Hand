from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    )
from . import views

urlpatterns = [
    path('', views.index, name='ads-index'),
    path('ads/', PostListView.as_view(), name='ads-list'),
    path('ads/new/', PostCreateView.as_view(), name='ads-create'),
    path('ads/<int:pk>', PostDetailView.as_view(), name='ads-detail'),
]