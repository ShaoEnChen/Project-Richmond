# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from datetime import datetime
from .models import trade
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

			end_price = 
			buy_price = 
			sell_price = 
			total_num = 
			yesterday_end = 
			start_price = 
			high_price = 
			low_price = 
			change = round(float(end_price) - float(yesterday_end), 2)
			stock_info = "詳細內容"
			info_url = "https://tw.finance.yahoo.com/q/ts?s="
			info_url += stock_id

			return render(request, 'trade/stock.html', {
				'stock_id': stock_id,
				'current_time': current_time,
				'end_price': end_price,
				'buy_price': buy_price,
				'sell_price': sell_price,
				'change': change,
				'total_num': total_num,
				'yesterday_end': yesterday_end,
				'start_price': start_price,
				'high_price': high_price,
				'low_price':low_price,
				'stock_info': stock_info,
				'url': url,
				'info_url': info_url,
			})
		else:
			return redirect(select_stock_view, permanent = True)
	else:
		return redirect(select_stock_view, permanent = True)

def add_trade(request):
	if request.method == 'POST' and 'stock_id' in request.POST:
		stock_id = request.POST['stock_id']
		if 'buysell' in request.POST and 'vol' in request.POST and request.POST['vol'] != '':
			# get current time in Taipei
			utcnow = datetime.utcnow()
			tpe = pytz.timezone('Asia/Taipei')
			current_time = tpe.fromutc(utcnow)

			trade.objects.create(player_name = request.user, trade = request.POST['buysell'], trade_company = stock_id, trade_num = request.POST['vol'])
			return redirect(select_stock_view, permanent = True)
		else:
			return redirect('/stock/?stock_id=' + stock_id)
	else:
		return redirect(select_stock_view, permanent = True)
