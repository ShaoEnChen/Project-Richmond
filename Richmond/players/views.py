from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from players.models import Profile

def register_view(request):
	return render(request, 'account/register.html')

def login(request):
	if request.user.is_authenticated():
		return redirect('/', permanent = True)

	msg = ''

	if request.method == 'POST':
		try:
			username = request.POST['username']
			password = request.POST['password']
			if not username:
				msg += '請輸入帳號，'
			if not password:
				msg += '請輸入密碼，'
			user = auth.authenticate(username = username, password = password)
		except:
			msg = '登入失敗，請輸入英文或數字！'
			return render(request, 'account/login.html', {
				'msg': msg
			})
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('/', permanent = True)
		else:
			msg += '登入失敗！'
			return render(request, 'account/login.html', {
				'msg': msg
			})

	return render(request, 'account/login.html', {
		'msg': msg
	})

def register(request):
	if request.method == 'POST':
		uform = UserCreationForm(request.POST)
		if uform.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password1']
			user = User.objects.create_user(username, email, password)
			user.save()
			user_profile = Profile(user = user)
			user_profile.save()
			# perhaps set permissions of the new user
			return redirect('/accounts/login', permanent = True)
	else:
		form = UserCreationForm()
	return redirect('/accounts/login/register', permanent = True)

def user_view(request):
	user_list = User.objects.all().exclude(username__exact = request.user.username)
	return render(request, 'account/user_list.html', {
		'user_list': user_list
	})