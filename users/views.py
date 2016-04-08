
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponse
from users.models import Post
from users.forms import CreatePostForm, UpdatePostForm, UserForm, UserProfileForm
from django.views.generic import View
from django.contrib.auth import authenticate, login

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


class User_Register(View):
	template = "registration.html"

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, "index.html", {})
		user_form = UserForm()
		profile_form = UserProfileForm()
		context = {
			'user_form': user_form,
			'profile_form': profile_form
		}
		return render(request, self.template, context)

	def post(self, request):
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()
			#Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			profile = profile_form.save(commit=False)
			profile.user = user
			# Now we save the UserProfile model instance.
			profile.save()
			return redirect('/')
		else:
			context = {
				'user_form': user_form,
				'profile_form': profile_form
			}
			return render(request, self.template, context)
			
class User_Login(View):
	template = "login.html"

	def post(self, request):
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return redirect('/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Mini-Twitter account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	def get(self, request):
		return render(request, 'login.html', {})
















# def create(request):
# 	if request.method == 'GET':
# 		context = {
# 			'form': CreatePostForm()
# 		}
# 		return render(request, 'posts/create.html', context)
# 	elif request.method == 'POST':
# 		form = CreatePostForm(data=request.POST)
# 		if form.is_valid():
# 			posts = form.save()
# 			return redirect('posts:home')
# 		context = {
# 			'form': form
# 		}
# 		return render(request, 'posts/create.html', context)
# 	else:
# 		return HttpResponseNotAllowed(['GET','POST'])

# def update(request, pk):
# 	if request.method == 'GET':
# 		posts = Post.objects.get(pk=pk)
# 		context = {
# 			'form': UpdatePostForm(instance=posts),
# 			'posts': posts
# 		}
# 		return render(request, 'posts/update.html', context)
# 	elif request.method == 'POST':
# 		posts = Post.objects.get(pk=pk)
# 		form = UpdatePostForm(data=request.POST, instance=posts)
# 		if form.is_valid():
# 			posts = form.save()
# 			return redirect('posts:home')
# 		context = {
# 			'form': form,
# 			'posts': posts
# 		}
# 		return render(request, 'posts/update.html', context)
# 	else:
# 		return HttpResponseNotAllowed(['GET', 'POST'])


# def delete(request, pk):
# 	if request.method == 'POST':
# 		posts = Post.objects.get(pk=pk)
# 		posts.delete()
# 		return redirect('posts:home')
# 	else:
# 		return HttpResponseNotAllowed(['POST'])

