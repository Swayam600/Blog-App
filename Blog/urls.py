from django.urls import *
from . import views


app_name = 'Blog'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('<int:post_id>/post/', views.post, name='1-post'),
    path('query/', views.query, name='searching'),
]
