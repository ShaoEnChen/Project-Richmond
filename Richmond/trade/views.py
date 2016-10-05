# This Python file uses the following encoding: utf-8
from django.shortcuts import render, redirect
from datetime import datetime
from players.models import Profile
from stock.models import Stock
# from stockheld.models import Holding_Stock
from .models import Trade
from cronjob.crawler import crawl
import re # REGEX
import pytz # time
import requests

'''
# REGEX to check GET
p = '^[0-9]+$'
pat = re.compile(p)
'''

def select_stock_view(request):
	return render(request, 'trade/select_stock.html')

def stock_view(request):
	try:
		stock_id = request.GET['stock_id']
		
		'''
		if request.method == 'GET' and 'stock_id' in request.GET:
			# get stock id...
		# compare stock_id with REGEX
		result = re.match(pat, stock_id)
		# if don't match, result returns None
		if result != None:
			# ...
		'''
		# query model for stock data
		query = "SELECT * FROM stock_stock WHERE stock_id = "
		query += stock_id
		query += " ORDER BY id DESC LIMIT 1;"
		query_stock = Stock.objects.raw(query)[0]
		
		end_price = query_stock.end_price
		yesterday_end = query_stock.yesterday_end
		change = round(float(end_price) - float(yesterday_end), 2)
		
		# get current time in 'Asia/Taipei'
		current_time = datetime.now()

		# references
		url = "https://tw.stock.yahoo.com/q/q?s="
		url += stock_id
		info_url = "https://tw.finance.yahoo.com/q/ts?s="
		info_url += stock_id

		return render(request, 'trade/stock.html', {
			'current_time': current_time,
			'stock_id': stock_id,
			'stock': query_stock,
			'change': change,
			'url': url,
			'info_url': info_url
		})
	except:
		return redirect(select_stock_view, permanent = True)

def add_trade(request):
	try:
		stock_id = request.POST['stock_id']
	except:
		return redirect(select_stock_view, permanent = True)
	try:
		bs = request.POST['buysell']
		vol = int(request.POST['vol'])
		price = request.POST['price']
	except:
		return redirect('/stock/?stock_id=' + stock_id, permanent = True)
		
	# get current time in Taipei
	current_time = datetime.now()

	# Assets increase/decrease due to transactions
	if bs == 'b':	# buy
		is_success = request.user.profile.assets_decrease(float(price), vol)
		# hstock_increase(float(vol))
	else:	# sell
		is_success = request.user.profile.assets_increase(float(price), vol)
		# hstock_decrease(float(vol))
	if is_success:
		# Create trade record
		Trade.objects.create(player_name = request.user.username, trade = bs, trade_company = stock_id, trade_num = vol)
	#	some success message
	# if not is_success:
	#	some fail message
	return redirect(select_stock_view, permanent = True)
	
def trade_record_view(request):
	username = request.user.username
	query = "SELECT * FROM trade_trade WHERE player_name = "
	query += "'"
	query += username
	query += "' ORDER BY id DESC"
	user_records = Trade.objects.raw(query)
	return render(request, 'trade/trade_record.html', {
		'username': username,
		'record_list': user_records
	})
