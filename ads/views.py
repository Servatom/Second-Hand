from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    )
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'ads/ads.html'
    context_object_name = 'posts'
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'price', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

def index(request):
    return render(request, 'ads/index.html')