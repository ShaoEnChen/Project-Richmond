# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from datetime import datetime
from players.models import Profile
from stock.models import Stock
# from stockheld.models import Holding_Stock
from .models import Trade
# from cronjob.crawler import crawl
# import re # REGEX
# import pytz # time
# import requests

'''
# REGEX to check GET
p = '^[0-9]+$'
pat = re.compile(p)
'''

def select_stock_view(request):
	return render(request, 'trade/select_stock.html')

def stock_view(request):
	msg = ''
	if request.method == 'GET' and 'stock_id' in request.GET:
		stock_id = request.GET['stock_id']
	else:
		stock_id = None
	
	# access stock from db
	stock = Stock.getNewestStock(stock_id)
	
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
	
	# get record info
	if 'buysell' in request.POST and 'vol' in request.POST and 'price' in request.POST:
		bs = request.POST['buysell']
		vol = int(request.POST['vol'])
		price = float(request.POST['price'])
	else:
		return redirect('/stock/?stock_id=' + stock_id, permanent = True)

	try:
		# Assets increase/decrease due to transactions
		if bs == 'b':	# buy
			is_buy = True
			is_success = request.user.profile.assets_decrease(float(price), vol)
			# hstock_increase(float(vol))
		elif bs == 's':	# sell
			is_buy = False
			is_success = request.user.profile.assets_increase(float(price), vol)
			# hstock_decrease(float(vol))
		else:
			is_success = False

		if is_success:
			# Create trade record
			Trade.objects.create(player_name = request.user.username, is_buy = is_buy, trade_company = stock_id, trade_num = vol)
		#	some success message
		# if not is_success:
		#	some fail message
	except:
		pass

	return redirect(select_stock_view, permanent = True)
	
def trade_record_view(request):
	username = request.user.username
	user_records = Trade.objects.filter(player_name__exact = username).order_by('-created_at')
	return render(request, 'trade/trade_record.html', {
		'username': username,
		'record_list': user_records
	})
