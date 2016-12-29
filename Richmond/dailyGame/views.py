#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Game, JoinedPlayer, GameRecord
from stock.models import Stock
from players.models import Profile
from notification.models import Notification

def daily_game_view(request):
	try:
		game = Game.objects.get(is_active__exact=True)
	except Game.DoesNotExist:
		game = None
	return render(request, 'dailyGame/bulletin.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count(),
		'game': game
	})

def join_game(request):
	if request.method == 'POST' and 'cost' in request.POST:
		game_cost = float(request.POST['cost'])
		if request.user.profile.is_in_daily_game == False and request.user.profile.assets_decrease(game_cost, 1):
			request.user.profile.is_in_daily_game = True
			request.user.profile.save()
			JoinedPlayer.objects.create(player = request.user, init_assets = request.user.profile.assets)
			return redirect(playground_view, permanent = True)
		else:
			return redirect('/dailyGame/', permanent = True)
	else:
		return redirect('/dailyGame/', permanent = True)

def playground_view(request):
	stock_id = "2330"
	msg = ''
	# access stock from db
	stock = Stock().getNewestStock(stock_id)

	# get price change from stock
	try:
		# get full info of stock
		end_price = stock.end_price
		yesterday_end = stock.yesterday_end
		change = round(float(end_price) - float(yesterday_end), 2)
	except:
		msg += '錯誤：無法取得股票漲跌資訊\n'
		change = ''

	# get time
	try:
		# get current time in 'Asia/Taipei'
		current_time = datetime.now()
	except:
		msg += '錯誤：無法取得時間\n'
		current_time = ''

	return render(request, 'dailyGame/playground.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count(),
		'stock': stock,
		'change': change,
		'current_time': current_time,
		'msg': msg
	})

def add_game_record(request):
	stock_id = "2330"
	if request.method == 'POST':
		# get record info
		if 'buysell' in request.POST:
			bs = request.POST['buysell']
		else:
			bs = None
		if 'vol' in request.POST:
			vol = int(request.POST['vol'])
		else:
			vol = 0
		if 'price' in request.POST:
			price = float(request.POST['price'])
		else:
			price = 0

		# create player's game record
		try:
			current_user = request.user

			# Assets increase/decrease due to transactions
			if bs == 'b':	# buy
				is_buy = True
				is_success = current_user.profile.assets_decrease(price, vol)
				# hstock_increase(float(vol))
			elif bs == 's':	# sell
				is_buy = False
				is_success = current_user.profile.assets_increase(price, vol)
				# hstock_decrease(float(vol))
			else:
				is_success = False

			if is_success:
				# Create record
				GameRecord.objects.create(player = request.user, is_buy = is_buy, trade_num = vol)
			#	some success message
			# if not is_success:
			#	some fail message
		except:
			pass

	return redirect(playground_view, permanent = True)