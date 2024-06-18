from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def admin_dashboard(request):
    posts = Post.objects.filter(author=request.user)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('admin-dashboard')
    return render(request, 'admin.html', {'form': form, 'posts': posts,'page_title':'Add New Post','b_name':'Add Post'})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    return render(request, 'admin.html', {'form': form,'page_title':'Update Post','b_name':'Update Post'})


def delete_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect(reverse('my_posts'))
    else:
        posts = Post.objects.all()
        return render(request, 'my_post.html', {'posts': posts})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_form(request):
    return render(request,'registration/login.html')

def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'my_post.html', {'posts': posts})