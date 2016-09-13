from django.db import models

class stock(models.Model):
	stock_id = models.CharField(max_length=10)
	time = models.DateTimeField(auto_now_add=True)
	end_price = models.FloatField()
	buy_price = models.FloatField()
	sell_price = models.FloatField()
	total_num = models.IntegerField()
	yesterday_end = models.FloatField()
	start_price = models.FloatField()
	high_price = models.FloatField()
	low_price = models.FloatField()
	def __str__(self):
		return "%s %s" % self.time % self.stock_id