from django.shortcuts import render
from .models import Game

def daily_game_view(request):
	game_list = Game.objects.all()
	return render(request, 'dailyGame/bulletin.html', {
		'game_list': game_list
	})