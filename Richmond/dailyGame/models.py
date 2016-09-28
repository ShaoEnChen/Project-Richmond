from django.db import models

class Game(models.Model):
	title = models.CharField(max_length=50)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return "game %s" % self.title