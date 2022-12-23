from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from blog.forms import PostForm
from blog.models import Post


def index(request):
    return render(request, 'index.html')


# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.author = request.user.profile
            post.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('ERROR')
    else:
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})

def view_posts(request):
    search = request.GET.get('search')
    # get all posts frome the database
    if search:
        posts = Post.objects.filter(Q(title__contains=search) | Q(text__contains=search)).order_by('-created_date')
    else:
        posts = Post.objects.all().order_by('-created_date')
    return render (request, 'view_posts.html', {'posts': posts, 'title': "All Posts"})