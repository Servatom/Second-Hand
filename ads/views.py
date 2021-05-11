from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    )
from .models import Post
from users.models import CustomUser


class PostListView(ListView):
    model = Post
    template_name = 'ads/ads.html'
    context_object_name = 'posts'
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'description', 'price', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'description', 'price', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('ads-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostSearchView(ListView):
    model = Post
    template_name = 'ads/ads.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        ad_list = Post.objects.filter(Q(title__icontains=query))
        return ad_list

class UserAdList(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Post
    template_name = 'ads/user_ads.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(CustomUser, email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def test_func(self):
        if str(self.request.user) == self.kwargs.get('email'):
            return True
        return False

def index(request):
    return render(request, 'ads/index.html')