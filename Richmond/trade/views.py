from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from .models import trade # models (database)
import re # REGEX
import pytz # time
import requests

# REGEX to check GET
p = '^[0-9]+$'
pat = re.compile(p)

def home(request):
	return render(request, 'home.html')

def showStock(request):
	if request.method == 'GET' and 'stock_id' in request.GET:
		stock_id = request.GET['stock_id']
		# compare stock_id with REGEX
		result = re.match(pat, stock_id)
		# if don't match, result returns None
		if result != None:
			# get current time in Taipei
			utcnow = datetime.utcnow()
			tpe = pytz.timezone('Asia/Taipei')
			current_time = tpe.fromutc(utcnow)

			# crawling Yahoo!Stock
			url = "https://tw.stock.yahoo.com/q/q?s="
			url += stock_id
			headers = {
				'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
			}
			page = requests.get(url, headers = headers).text
			# crawl pattern
			crawl_p = '<td align="center" bgcolor="#FFFfff" nowrap>(.*?)</td>'
			crawl_pat = re.compile(crawl_p)
			# list
			result = crawl_pat.findall(page)

			end_price = result[1]
			buy_price = result[2]
			sell_price = result[3]
			change = ""
			total_num = result[4]
			yesterday_end = result[5]
			start_price = result[6]
			high_price = result[7]
			low_price = result[8]
			stock_info = "詳細內容"
			info_url = "https://tw.finance.yahoo.com/q/ts?s="
			info_url += stock_id

			return render(request, 'stock.html', {
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
			return redirect(home, permanent = True)
	else:
		return redirect(home, permanent = True)

def addTrade(request):
	if request.method == 'POST' and 'stock_id' in request.POST:
		stock_id = request.POST['stock_id']
		if 'buysell' in request.POST and 'vol' in request.POST and request.POST['vol'] != '':
			# get current time in Taipei
			utcnow = datetime.utcnow()
			tpe = pytz.timezone('Asia/Taipei')
			current_time = tpe.fromutc(utcnow)

			trade.objects.create(player_name = 'sean', trade = request.POST['buysell'], trade_company = stock_id, trade_num = request.POST['vol'], created_at = current_time)
			return redirect(home, permanent = True)
		else:
			return redirect('/stock/?stock_id=' + stock_id)
	else:
		return redirect(home, permanent = True)