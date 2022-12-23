from django.urls import path
from blog.views import add_post, view_posts, index

urlpatterns = [
    path('post/add', add_post),
    path('posts/', view_posts),
    path('index/', index)
]