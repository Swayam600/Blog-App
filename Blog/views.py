from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            print('User cannot be created')
            return render(request, 'user-register.html', {'message': 'This username has been taken'})

        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            auth.login(request, new_user)

            
            
    return render(request, 'home.html')

    

def posts(request):
    context = {
        'posts': Post.objects.all()[:5:-1],
    }
    return render(request, 'posts.html', context)

def post(request, post_id):
    context = {
        'post': Post.objects.get(id = post_id)
    }

    return render(request, 'post.html', context)

def query(request):

    if request.method == "POST":
        name = request.POST.get('username')
        title = request.POST.get('title')
        content = request.POST.get('content')

        new_post = Post(Username=name, Title=title, Content=content)
        new_post.save()
        return render(request, 'query_post.html', {'message': 'Your post has been uploaded.'})

    return render(request, 'query_post.html')