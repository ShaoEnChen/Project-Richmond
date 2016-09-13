from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from .models import UserForm
from .models import ProfileForm

def login_view(request):
	return render(request, 'account/login.html')

def register_view(request):
	return render(request, 'account/register.html')

def login(request):
	if request.user.is_authenticated():
		return redirect('/', permanent = True)
	
	username = request.POST['username']
	password = request.POST['password']
	
	user = auth.authenticate(username = username, password = password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return redirect('/', permanent = True)
	else:
		return redirect('/accounts/login', permanent = True)

def register(request):
	if request.method == 'POST':
		uform = UserForm(request.POST, prefix = "user")
		pform = ProfileForm(request.POST, prefix = "userprofile")
		if uform.is_valid() * pform.is_valid():
			new_user = uform.save()
			userprofile = pform.save(commit = False)
			userprofile.user = new_user
			userprofile.save()
			# perhaps set permissions of the new user
			return redirect('/accounts/login', permanent = True)
	return redirect('/accounts/login/register', permanent = True)
