from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True
	)
	assets = models.FloatField(default = 300000.00)
	exp = models.IntegerField(default = 0)
	is_in_daily_game = models.BooleanField(default = False)
	
	def __str__(self):
		return "%s's profile" % self.user.username

	def assets_increase(self, price, vol):
		assets = self.assets
		assets += price * vol
		return assets

	def assets_decrease(self, price, vol):
		assets = self.assets
		if assets >= price * vol:
			assets -= price * vol
			return assets
