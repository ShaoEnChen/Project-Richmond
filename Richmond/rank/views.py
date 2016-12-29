from django.shortcuts import render
from django.contrib.auth.models import User
from trade.models import Trade
from datetime import date, timedelta
from operator import itemgetter
from notification.models import Notification

def rank_view(request):
	user_list = User.objects.all()

	# week rank
	rank_list_week = []
	for user in user_list:
		try:
			trade = Trade.objects.filter(player_name = user.username, created_at__date__lte = (date.today() - timedelta(days = date.today().isoweekday()))).order_by('-created_at')
			temp = trade[:1].get()
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - temp.cur_assets) / temp.cur_assets * 100)
			rank_list_week.append(rank)
		except Exception:
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - 300000) / 300000 * 100)
			rank_list_week.append(rank)
	rank_list_week.sort(key = lambda elem : elem[2], reverse=True)

	# month rank
	rank_list_month = []
	for user in user_list:
		try:
			trade = Trade.objects.filter(player_name = user.username, created_at__date__lte = (date.today() - timedelta(days = date.today().day))).order_by('-created_at')
			temp = trade[:1].get()
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - temp.cur_assets) / temp.cur_assets * 100)
			rank_list_month.append(rank)
		except Exception:
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - 300000) / 300000 * 100)
			rank_list_month.append(rank)
	rank_list_month.sort(key = lambda elem : elem[2], reverse=True)

	# season rank
	rank_list_season = []
	for user in user_list:
		try:
			season_order = (date.today().month - 1) // 3 + 1
			if season_order == 1:
				dayscounter = date.today() - date(date.today().year, 1, 1)
			elif season_order == 2:
				dayscounter = date.today() - date(date.today().year, 4, 1)
			elif season_order == 3:
				dayscounter = date.today() - date(date.today().year, 7, 1)
			elif season_order == 4:
				dayscounter = date.today() - date(date.today().year, 10, 1)
			trade = Trade.objects.filter(player_name = user.username, created_at__date__lte = (date.today() - timedelta(days = dayscounter))).order_by('-created_at')
			temp = trade[:1].get()
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - temp.cur_assets) / temp.cur_assets * 100)
			rank_list_season.append(rank)
		except Exception:
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - 300000) / 300000 * 100)
			rank_list_season.append(rank)
	rank_list_season.sort(key = lambda elem : elem[2], reverse=True)

	# year rank
	rank_list_year = []
	for user in user_list:
		try:
			trade = Trade.objects.filter(player_name = user.username, created_at__date__lte = (date.today() - timedelta(days = date.today() - date(date.today().year, 1, 1)))).order_by('-created_at')
			temp = trade[:1].get()
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - temp.cur_assets) / temp.cur_assets * 100)
			rank_list_year.append(rank)
		except Exception:
			rank = []
			rank.append(user.username)
			rank.append(user.profile.exp)
			rank.append((user.profile.assets - 300000) / 300000 * 100)
			rank_list_year.append(rank)
	rank_list_year.sort(key = lambda elem : elem[2], reverse=True)

	return render(request, 'rank.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count(),
		'rank_list_week': rank_list_week,
		'rank_list_month': rank_list_month,
		'rank_list_season': rank_list_season,
		'rank_list_year': rank_list_year
	})