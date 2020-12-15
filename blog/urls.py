
from django.urls import path
from . import views # . is for current directory

# we are already in blog/ so only next part is included
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

