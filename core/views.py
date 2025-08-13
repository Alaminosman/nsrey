from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()  # Fetches all Post objects from the database
    return render(request, 'core/home.html', {'posts': posts})

# Create your views here.
