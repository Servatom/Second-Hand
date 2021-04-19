from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='ads-index'),
    path('about/', views.about, name='ads-about'),
    path('ads/', views.ads, name='ads-list')
]