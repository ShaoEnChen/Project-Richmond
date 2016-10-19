from django.shortcuts import render, redirect
from notification.models import Notification
from .models import PKGame

def invite_pk(request):
	if request.method == 'POST':
		if 'invitee' in request.POST and 'timespan' in request.POST and 'mode' in request.POST:
			yourname = request.user.username
			invitee = request.POST['invitee']
			timespan = request.POST['timespan']
			mode = request.POST['mode']

			# get mode name
			mode_name = PKGame.PK_MODE[int(mode)-1][1]

			invite_content = Notification.get_invite_pk_content(yourname, timespan, mode_name)
			Notification.objects.create(n_type = Notification.INVITATION, n_from = yourname, n_to = invitee, content = invite_content)
			PKGame.objects.create(invitor = yourname, invitee = invitee, mode = mode)

	return redirect('/', permanent = True)

# def confirm_pk(request):
