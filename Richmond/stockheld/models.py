from players.models import Profile
from stock.models import Stock
from django.db import models

class Holding_Stock(models.Model):
	player_name = models.CharField(max_length = 100)
	s_id = models.CharField(max_length = 10)
	hstock = models.IntegerField(default = 0)
	def __str__(self):
		return "%s's %s" % (self.player_name, self.s_id)

	def hstock_increase(self, vol):
		self.hstock += vol
		self.save()
		return True

	def hstock_decrease(self, vol):
		if self.hstock >= vol:
			self.hstock -= vol
			self.save()
			return True
		else:
			return False
