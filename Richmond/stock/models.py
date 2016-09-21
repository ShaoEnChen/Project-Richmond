from django.db import models

class Stock(models.Model):
	stock_id = models.CharField(max_length=10)
	time = models.DateTimeField(auto_now_add=True)
	end_price = models.CharField(max_length=10)
	buy_price = models.CharField(max_length=10)
	sell_price = models.CharField(max_length=10)
	total_num = models.CharField(max_length=10)
	yesterday_end = models.CharField(max_length=10)
	start_price = models.CharField(max_length=10)
	high_price = models.CharField(max_length=10)
	low_price = models.CharField(max_length=10)
	def __str__(self):
		return "%s %s" % (self.time, self.stock_id)