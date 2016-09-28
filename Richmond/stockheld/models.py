from django.db import models

class Holding_Stock(models.Model):
	player_name = models.CharField(max_length=100)
	stock_id = models.CharField(max_length=10)
	hold_num = models.CharField(max_length=10)