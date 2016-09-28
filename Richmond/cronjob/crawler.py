from stock.models import Stock
from .models import Cron_Job_Log
import logging
import requests
import re

# TW50, ref: http://www.cnyes.com/twstock/Etfingredient/0050.htm
# '3697' removed
stocklist = ['1101', '1102', '1216', '1301', '1303', '1326', '1402', '1722', '2002', '2105', '2201', '2207', '2301', '2303', '2308', '2311', '2317', '2324', '2325', '2330', '2347', '2353', '2354', '2357', '2382', '2409', '2412', '2454', '2474', '2498', '2801', '2880', '2881', '2882', '2883', '2885', '2886', '2890', '2891', '2892', '2912', '3008', '3045', '3231', '3481', '3673', '4904', '5880', '6505'] 
# crawl pattern
crawl_p = '<td align="center" bgcolor="#FFFfff" nowrap>(.*?)</td>'
trunc_p = '<.*?>'
logger = logging.getLogger('cronjob.crawler')

def crawl():
	# Set logger
	job = Cron_Job_Log()
	job.title = crawl.__name__
	try:
		# Crawling Yahoo! Stock
		headers = {
			'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
		}
		for stock_id in stocklist:
			url = "https://tw.stock.yahoo.com/q/q?s="
			url += stock_id
			page = requests.get(url, headers = headers).text
			
			crawl_pat = re.compile(crawl_p)
			result = crawl_pat.findall(page) # list
			
			trunc_pat = re.compile(trunc_p)
			for i in range(len(result)):
				result[i] = trunc_pat.sub('', result[i])

			# Create and save an object in a single step
			Stock.objects.create(
				stock_id = stock_id,
				end_price = result[1],
				buy_price = result[2],
				sell_price = result[3],
				total_num = result[4],
				yesterday_end = result[5],
				start_price = result[6],
				high_price = result[7],
				low_price = result[8]
			)
	except:
		logger.warning("Error perform cron job %s" % sys._getframe().f_code.co_name, exc_info=1)
		job.failed()
		raise
	else:
		job.success()
	finally:
		job.save()
