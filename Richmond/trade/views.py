# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from datetime import datetime
from players.models import Profile
from stock.models import Stock
from .models import Trade
from cronjob.crawler import crawl
import re # REGEX
import pytz # time
import requests

# REGEX to check GET
p = '^[0-9]+$'
pat = re.compile(p)

def select_stock_view(request):
	return render(request, 'trade/select_stock.html')

def stock_view(request):
	if request.method == 'GET' and 'stock_id' in request.GET:
		stock_id = request.GET['stock_id']
		# compare stock_id with REGEX
		result = re.match(pat, stock_id)
		# if don't match, result returns None
		if result != None:
			# get current time in 'Asia/Taipei'
			current_time = datetime.now()
			
			# query model for stock data
			query = "SELECT * FROM stock_stock WHERE stock_id = "
			query += stock_id
			query += " ORDER BY id DESC LIMIT 1;"
			query_stock = Stock.objects.raw(query)[0]
			
			end_price = query_stock.end_price
			yesterday_end = query_stock.yesterday_end
			change = round(float(end_price) - float(yesterday_end), 2)
			stock_info = "詳細內容"
			url = "https://tw.stock.yahoo.com/q/q?s="
			url += stock_id
			info_url = "https://tw.finance.yahoo.com/q/ts?s="
			info_url += stock_id

			return render(request, 'trade/stock.html', {
				'stock_id': stock_id,
				'current_time': current_time,
				'end_price': end_price,
				'buy_price': query_stock.buy_price,
				'sell_price': query_stock.sell_price,
				'change': change,
				'total_num': query_stock.total_num,
				'yesterday_end': yesterday_end,
				'start_price': query_stock.start_price,
				'high_price': query_stock.high_price,
				'low_price': query_stock.low_price,
				'stock_info': stock_info,
				'url': url,
				'info_url': info_url
			})
		else:
			return redirect(select_stock_view, permanent = True)
	else:
		return redirect(select_stock_view, permanent = True)

def add_trade(request):
	if request.method == 'POST' and 'stock_id' in request.POST:
		stock_id = request.POST['stock_id']
		if 'buysell' in request.POST and 'vol' in request.POST and request.POST['vol'] != '':
			bs = request.POST['buysell']
			vol = request.POST['vol']
			price = request.POST['price']
			# get current time in Taipei
			current_time = datetime.now()

			# Create trade record
			Trade.objects.create(player_name = request.user, trade = bs, trade_company = stock_id, trade_num = vol)
			# Assets increase/decrease due to transactions
			if bs == 'b':	# buy
				is_success = request.user.profile.assets_decrease(float(price), float(vol))
			else:	# sell
				is_success = request.user.profile.assets_increase(float(price), float(vol))
			# if not is_success:
			#	some message	
			return redirect(select_stock_view, permanent = True)
		else:
			return redirect('/stock/?stock_id=' + stock_id)
	else:
		return redirect(select_stock_view, permanent = True)

def trade_record_view(request):
	username = request.user.username
	query = "SELECT * FROM trade_trade WHERE player_name = "
	query += "'"
	query += username
	query += "'"
	user_records = Trade.objects.raw(query)
	return render(request, 'trade/trade_record.html', {
		'username': username,
		'record_list': user_records
	})
