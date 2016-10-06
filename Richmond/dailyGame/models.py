from django.db import models
from datetime import datetime
# from players.models import Profile
from django.contrib.auth.models import User

class Game(models.Model):
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	cost = models.FloatField(default=10000.0)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.title

# class JoinedPlayer
class JoinedPlayer(models.Model):
	player = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	init_assets = models.FloatField(editable=False, default=300000.0)
	def __str__(self):
		return self.player.username

# class GameRecord
class GameRecord(models.Model):
	player = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
	)
	# buy(b) or sell(s)
	is_buy = models.BooleanField(default=True)
	trade_num = models.IntegerField()
	created_at = models.DateTimeField(default=datetime.now())
	def __str__(self):
		return "%s's record" % self.player.username