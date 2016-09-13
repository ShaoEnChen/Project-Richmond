from django.db import models

class trade(models.Model):
	player_name = models.CharField(max_length=100)
	# buy(b) or sell(s)
	trade = models.CharField(max_length=1)
	trade_company = models.CharField(max_length=5)
	trade_num = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%s's trde" % self.player_name
