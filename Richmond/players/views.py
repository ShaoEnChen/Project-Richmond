#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from players.models import Profile
from pk.models import PKGame
from stockheld.models import Holding_Stock

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

			#Create empty holding stock list
			stocklist = ['1101', '1102', '1216', '1301', '1303', '1326', '1402', '1722', '2002', '2105', '2201', '2207', '2301', '2303', '2308', '2311', '2317', '2324', '2325', '2330', '2347', '2353', '2354', '2357', '2382', '2409', '2412', '2454', '2474', '2498', '2801', '2880', '2881', '2882', '2883', '2885', '2886', '2890', '2891', '2892', '2912', '3008', '3045', '3231', '3481', '3673', '4904', '5880', '6505']
			for stock_id in stocklist:
				Holding_Stock.objects.create(player_name = username, s_id = stock_id)

			return redirect('/accounts/login', permanent = True)
	else:
		form = UserCreationForm()

	return redirect('/accounts/login', permanent = True)

def user_view(request):
	user_list = User.objects.all().exclude(username__exact = request.user.username)
	return render(request, 'account/user_list.html', {
		'user_list': user_list,
		'pk_mode': PKGame.PK_MODE
	})

# def subscribe_user(request):
# 	user = request['subscribe_user'] || ''
# 	if user != '':


# def follow_user(request):

