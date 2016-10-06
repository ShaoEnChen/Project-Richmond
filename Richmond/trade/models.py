from datetime import datetime
from django.db import models

class Trade(models.Model):
	player_name = models.CharField(max_length=100)
	# buy(b) or sell(s)
	is_buy = models.BooleanField(default=True)
	trade_company = models.CharField(max_length=5)
	trade_num = models.IntegerField()
	created_at = models.DateTimeField(default=datetime.now())
	def __str__(self):
		return "%s's trade" % self.player_name