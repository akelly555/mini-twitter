
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from posts.models import Post
from posts.forms import CreatePostForm, UpdatePostForm

# Create your views here.

def index(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		context = {
			'posts': posts
		}
		return render(request, 'posts/index.html', context)
	else:
		return HttpResponseNotAllowed


def create(request):
	if request.method == 'GET':
		context = {
			'form': CreatePostForm()
		}
		return render(request, 'posts/create.html', context)
	elif request.method == 'POST':
		form = CreatePostForm(data=request.POST)
		if form.is_valid():
			posts = form.save()
			return redirect('posts:home')
		context = {
			'form': form
		}
		return render(request, 'posts/create.html', context)
	else:
		return HttpResponseNotAllowed(['GET','POST'])


def update(request, pk):
	if request.method == 'GET':
		posts = Post.objects.get(pk=pk)
		context = {
			'form': UpdatePostForm(instance=posts),
			'posts': posts
		}
		return render(request, 'posts/update.html', context)
	elif request.method == 'POST':
		posts = Post.objects.get(pk=pk)
		form = UpdatePostForm(data=request.POST, instance=posts)
		if form.is_valid():
			posts = form.save()
			return redirect('posts:home')
		context = {
			'form': form,
			'posts': posts
		}
		return render(request, 'posts/update.html', context)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])


def delete(request, pk):
	if request.method == 'POST':
		posts = Post.objects.get(pk=pk)
		posts.delete()
		return redirect('posts:home')
	else:
		return HttpResponseNotAllowed(['POST'])









