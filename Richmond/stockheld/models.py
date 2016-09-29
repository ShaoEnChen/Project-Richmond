from django.db import models

class Holding_Stock(models.Model):
	player_name = models.CharField(max_length=100)
	stock_id = models.CharField(max_length=10)
	hstock = models.FloatField(max_length=10 ,default = 0)

	def hstock_increase(self, vol):
		hstock = self.hstock
		hstock += vol
		return hstock

	def hstock_decrease(self, vol):
		hstock = self.hstock
		if hstock >= vol:
			hstock -= vol
		return hstock
