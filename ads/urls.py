from django.urls import path, include
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostSearchView,
    )
from . import views

urlpatterns = [
    path('', views.index, name='ads-index'),
    path('ads/', PostListView.as_view(), name='ads-list'),
    path('ads/new/', PostCreateView.as_view(), name='ads-create'),
    path('ads/<int:pk>', PostDetailView.as_view(), name='ads-detail'),
    path('ads/<int:pk>/update/', PostUpdateView.as_view(), name='ads-update'),
    path('ads/<int:pk>/delete/', PostDeleteView.as_view(), name='ads-delete'),
    path('ads/search', PostSearchView.as_view(), name='ads-search')
]