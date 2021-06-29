from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog
from .forms import CreateForm

# Create your views here.

def layout(request):
    blogs = Blog.objects
    return render(request, 'myapp/layout.html', {'blogs' :blogs})

# def new(request):
#     return render(request, 'myapp/new.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('layout')
    else:
        form = CreateForm()
        return render(request, 'myapp/new.html', {'form':form})