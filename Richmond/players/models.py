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
		self.assets += price * vol
		self.save()
		return True

	def assets_decrease(self, price, vol):
		if self.assets >= price * vol:
			self.assets -= price * vol
			self.save()
			return True
		else:
			return False
