from datetime import datetime
from django.db import models

class Trade(models.Model):
	player_name = models.CharField(max_length=100)
	# buy(b) or sell(s)
	trade = models.CharField(max_length=1)
	trade_company = models.CharField(max_length=5)
	trade_num = models.IntegerField()
	created_at = models.DateTimeField(default=datetime.now())
	def __unicode__(self):
		return "%s's trade" % self.player_name