from django.urls import path

from .views import PostList, PostDetail, UserCreationView

urlpatterns = [
    path('', PostList.as_view(), name='api-list'),
    path('<int:pk>/', PostDetail.as_view(), name='api-detail'),
    path('user/register/', UserCreationView.as_view(), name='api-register'),
]