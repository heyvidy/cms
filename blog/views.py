from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
	all_posts = Post.objects.all()
	return render(request, "home.html", {'all_posts' : all_posts})

def create_post(request):

	if not request.user.is_authenticated:
		return redirect("/login/")

	if request.method == "POST":
		form_title = request.POST['title']
		form_body = request.POST['body']
		new_post = Post.objects.create(title=form_title, body=form_body)
		print(new_post.title, new_post.body, new_post.timestamp, sep="\n")
		return redirect(f"/post/{new_post.id}/")

	return render(request, "create.html")

def post_page(request, post_id):
	post = Post.objects.get(id=post_id)
	return render(request, "post.html", {"post": post})


def signin(request):
	if request.method == "POST":
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)
		print(username, password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			print("Im in")
			login(request, user)
			return redirect("/")
	return render(request, "login.html")


def signup(request):

	if request.method == "POST":
		fullname = request.POST.get('fullname', None)	
		email = request.POST.get('email', None)	
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)	
		print(password)
		
		user_exists = User.objects.filter(username=username).exists()
		if not user_exists:
			user = User.objects.create_user(
				username = username,
				password = password,
				email = email,
				first_name = fullname.split()[0],
				last_name = " ".join(fullname.split()[1:])
			)
			login(request, user)
			return redirect("/")
		else:
			return HttpResponse("User already exists. Try new username.")

	return render(request, "signup.html")

def signout(request):
	logout(request)
	return redirect("/")
	