# from django.utils import timezone
from datetime import datetime
from django.db import models

class Stock(models.Model):
	stock_id = models.CharField(max_length=10)
	time = models.DateTimeField(default=datetime.now())
	end_price = models.CharField(max_length=10)
	buy_price = models.CharField(max_length=10)
	sell_price = models.CharField(max_length=10)
	total_num = models.CharField(max_length=10)
	yesterday_end = models.CharField(max_length=10)
	start_price = models.CharField(max_length=10)
	high_price = models.CharField(max_length=10)
	low_price = models.CharField(max_length=10)
	def __str__(self):
		return self.stock_id

	def getNewestStock(stock_id):
		try:
			stock = Stock.objects.filter(stock_id__exact=stock_id).order_by('-time')[0]
		except:
			stock = None
		finally:
			return stock
