from django.shortcuts import render

def index(request):
    return render(request, 'ads/index.html')

def about(request):
    return render(request, 'ads/about.html')