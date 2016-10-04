from django.db import models

class Game(models.Model):
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	cost = models.FloatField(default=10000.0)
	is_active = models.BooleanField(default=True)
	def __unicode__(self):
		return "game %s" % self.title
