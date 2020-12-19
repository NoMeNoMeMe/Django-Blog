from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from django.urls import path
from . import views  # . is for current directory

# we are already in blog/ so only next part is included
urlpatterns = [
    # pk for primary key, int for integers only
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
