from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'ads/ads.html'
    context_object_name = 'posts'
    

def index(request):
    return render(request, 'ads/index.html')

def about(request):
    return render(request, 'ads/about.html')

def ads(request):
    return render(request, 'ads/ads.html')