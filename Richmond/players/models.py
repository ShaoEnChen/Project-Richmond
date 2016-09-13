from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	email = models.EmailField()
	assets = models.FloatField(default = 100000.00)
	exp = models.IntegerField(default = 0)
	def __str__(self):
		return "%s's profile" % self.user.username

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'first_name', 'last_name']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']