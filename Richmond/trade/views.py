# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from datetime import datetime
from players.models import Profile
from stock.models import Stock
from stockheld.models import Holding_Stock
from .models import Trade
from notification.models import Notification
# from cronjob.crawler import crawl
# import re # REGEX
# import pytz # time
# import requests

'''
# REGEX to check GET
p = '^[0-9]+$'
pat = re.compile(p)
'''
LEGAL_STOCKS = ['1101', '1102', '1216', '1301', '1303', '1326', '1402', '1722', '2002', '2105', '2201', '2207', '2301', '2303', '2308', '2311', '2317', '2324', '2325', '2330', '2347', '2353', '2354', '2357', '2382', '2409', '2412', '2454', '2474', '2498', '2801', '2880', '2881', '2882', '2883', '2885', '2886', '2890', '2891', '2892', '2912', '3008', '3045', '3231', '3481', '3673', '4904', '5880', '6505']

def select_stock_view(request):
	return render(request, 'trade/select_stock.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count()
	})

def stock_view(request):
	msg = ''
	if request.method == 'GET' and 'stock_id' in request.GET:
		stock_id = request.GET['stock_id']
	else:
		stock_id = None

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

	return render(request, 'trade/stock.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count(),
		'stock_id': stock_id,
		'stock': stock,
		'change': change,
		'current_time': current_time,
		'msg': msg
	})

def add_trade(request):
	# get stock id
	if request.method == 'POST' and 'stock_id' in request.POST:
		stock_id = request.POST['stock_id']
	else:
		stock_id = None

	if stock_id not in LEGAL_STOCKS:
		return redirect(select_stock_view, permanent = True)

	# get record info
	if 'buysell' in request.POST and 'vol' in request.POST and 'price' in request.POST:
		bs = request.POST['buysell']
		try:
			vol = int(request.POST['vol'])
			price = float(request.POST['price'])
		except:
			vol = 0
			price = 0

	try:
		# Assets increase/decrease due to transactions
		if bs == 'b':	# buy
			is_buy = True
			holding = Holding_Stock.objects.filter(player_name__exact = request.user.username).get(s_id__exact = stock_id)
			check_stock_success = holding.hstock_increase(vol)
			if check_stock_success:
				is_success = request.user.profile.assets_decrease(float(price), vol)
			else:
				is_success = False
		elif bs == 's':	# sell
			is_buy = False
			holding = Holding_Stock.objects.filter(player_name__exact = request.user.username).get(s_id__exact = stock_id)
			check_stock_success = holding.hstock_decrease(vol)
			if check_stock_success:
				is_success = request.user.profile.assets_increase(float(price), vol)
			else:
				is_success = False
		else:
			is_success = False

		if is_success:
			# Create trade record
			Trade.objects.create(player_name = request.user.username, cur_assets = request.user.profile.assets, is_buy = is_buy, trade_company = stock_id, trade_num = vol)
		#	some success message
		# if not is_success:
		#	some fail message
	except:
		pass

	return redirect(select_stock_view, permanent = True)

def trade_record_view(request):
	if 'userRecord' in request.GET:
		username = request.GET['userRecord']
	else:
		username = request.user.username
	user_records = Trade.objects.filter(player_name__exact = username).order_by('-created_at')
	return render(request, 'trade/trade_record.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count(),
		'username': username,
		'record_list': user_records
	})
