from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
# Create your views here.

# blog Home page
def blog_home(request):

    return render(request, "blog_home.html")
# Blog/add_post
# @login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Blog/allposts/')
    else:
        form = PostForm()
        return render(request, "add_post.html", {'form': form})

# all posts
def all_posts(request):

    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "all_posts.html", { 'posts': posts })    
# post_item
def post_item(request, id):

    post = Post.objects.get(id=id)

    return render(request, "post_item.html", { 'post': post }) 
# delete_post
def delete_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id = id)
        post.delete()
    return redirect('/Blog/allposts/')
    