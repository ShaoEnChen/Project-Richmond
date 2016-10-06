from django.shortcuts import render, redirect
from datetime import datetime
from .models import Game, JoinedPlayer, GameRecord
from stock.models import Stock

def daily_game_view(request):
	try:
		game = Game.objects.get(is_active__exact=True)
	except Game.DoesNotExist:
		game = None
	return render(request, 'dailyGame/bulletin.html', {
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
	try:
		# query model for stock data
		query = "SELECT * FROM stock_stock WHERE stock_id = 2330 ORDER BY id DESC LIMIT 1;"
		query_stock = Stock.objects.raw(query)[0]
		
		end_price = query_stock.end_price
		yesterday_end = query_stock.yesterday_end
		change = round(float(end_price) - float(yesterday_end), 2)
		
		# get current time in 'Asia/Taipei'
		current_time = datetime.now()

		# references
		url = "https://tw.stock.yahoo.com/q/q?s=2330"
		info_url = "https://tw.finance.yahoo.com/q/ts?s=2330"

		return render(request, 'dailyGame/playground.html', {
			'current_time': current_time,
			'stock': query_stock,
			'change': change,
			'url': url,
			'info_url': info_url
		})
	except:
		return redirect(daily_game_view, permanent = True)

def add_game_record(request):
	stock_id = 2330
	try:
		bs = request.POST['buysell']
		vol = int(request.POST['vol'])
		price = request.POST['price']
		# get current time in Taipei
		current_time = datetime.now()

		# Assets increase/decrease due to transactions
		if bs == 'b':	# buy
			is_buy = True
			is_success = request.user.profile.assets_decrease(float(price), vol)
			# hstock_increase(float(vol))
		else:	# sell
			is_buy = False
			is_success = request.user.profile.assets_increase(float(price), vol)
			# hstock_decrease(float(vol))
		if is_success:
			# Create record
			GameRecord.objects.create(player = request.user, is_buy = is_buy, trade_num = vol)
		#	some success message
		# if not is_success:
		#	some fail message
		return redirect(playground_view, permanent = True)
	except:
		return redirect(playground_view, permanent = True)