from django.shortcuts import render, redirect
from .models import Game

def daily_game_view(request):
	try:
		game = Game.objects.get(is_active__exact=True)
	except Game.DoesNotExist:
		game = None
	return render(request, 'dailyGame/bulletin.html', {
		'game': game
	})

def join_game(request):
	if request.method == 'POST' and 'cost' in request.POST:
		game_cost = float(request.POST['cost'])
		if request.user.profile.is_in_daily_game == False and request.user.profile.assets_decrease(game_cost, 1):
			request.user.profile.is_in_daily_game = True
			request.user.profile.save()
			return render(request, 'dailyGame/playground.html')
		else:
			return redirect('/')
	else:
		return redirect('/dailyGame/')

def playground_view(request):
	return render(request, 'dailyGame/playground.html')