from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm
from comments.models import Comment

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
    # post = Post.objects.get(id=id)
    # content_type = ContentType.objects.get_for_model(Post)
    # obj_id = post.id
    # comments = Comment.objects.filter(content_type = content_type, object_id = obj_id)
    # instance = get_object_or_404(Post, id=id)
    # comments = Comment.objects.filter_by_instance(instance)
def post_item(request, id):
    instance = get_object_or_404(Post, id=id)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    form = CommentForm(request.POST or None, initial = initial_data)
    
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model = c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None

        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj
        )
        return redirect('/Blog/allposts/')

    comments = instance.comments
    context = {
        'instance': instance,
        'comments': comments,
        'comment_form': form,        
    }

    return render(request, "post_item.html", context) 
# delete_post
def delete_post(request, id):
    
    if request.method == 'POST':
        post = Post.objects.get(id = id)
        if request.user.username == post.author:
            post.delete()
        else: 
            print(123)
            return redirect('/Blog/allposts/')   
    return redirect('/Blog/allposts/')
    