from django.shortcuts import render, redirect
from datetime import datetime
from .models import Notification
from pk.models import PKGame

def notification_view(request):
	me = request.user.username
	notif_list = Notification.objects.filter(n_to__exact = me).filter(is_read__exact = False).order_by('-created_at')
	try:
		is_empty = notif_list[0]
	except:
		is_empty = None
	return render(request, 'account/notifications.html', {
		'NOTIF_TYPE': dict(Notification.NOTIF_TYPE),
		'notif_list': notif_list,
		'is_empty': is_empty
	})

def invite_pk(request):
	if request.method == 'POST':
		if 'invitee' in request.POST and 'timespan' in request.POST and 'mode' in request.POST:
			yourname = request.user.username
			invitee = request.POST['invitee']
			timespan = request.POST['timespan']
			mode = request.POST['mode']

			# get mode name
			mode_name = PKGame.PK_MODE[int(mode)-1][1]

			# send invitation to invitee
			content = Notification.get_invite_pk(yourname, timespan, mode_name)
			Notification.objects.create(
				n_type = Notification.INVITATION,
				n_from = yourname,
				n_to = invitee,
				content = content
			)
			# create a pk game
			PKGame.objects.create(
				invitor = yourname,
				invitee = invitee,
				invitor_init_assets = request.user.profile.assets,
				life = timespan,
				mode = mode
			)

	return redirect('/', permanent = True)

def reply_invitation(request):
	if request.method == 'POST' and 'id' in request.POST and 'invitor' in request.POST and 'invitation_created_at' in request.POST and 'action' in request.POST:
		notif = Notification.objects.get(id__exact = request.POST['id'])
		notif.set_is_read()

		yourname = request.user.username
		invitor = request.POST['invitor']
		invitation_created_at = datetime.strptime(request.POST['invitation_created_at'], '%B %d, %Y, %I:%M %p')
		action = request.POST['action']

		# create notification to invitor
		content = Notification.invitee_pk_response(action, yourname)
		Notification.objects.create(
			n_type = Notification.ALARM,
			n_from = yourname,
			n_to = invitor,
			content = content
		)

		# change pk-game setting
		if action == '接受':
			accept_pk(request, invitor, yourname, invitation_created_at)
		elif action == '拒絕':
			decline_pk(request, invitor, yourname, invitation_created_at)

		# send your response of invitation back to you
		Notification.objects.create(
			n_type = Notification.ALARM,
			n_to = request.user.username,
			content = Notification.your_pk_response(action, notif.n_from)
		)
	return redirect('/', permanent = True)

def accept_pk(request, invitor, invitee, invitation_created_at):
	# accepted, start pk
	pkgame = PKGame.objects.filter(
		invitor__exact = invitor,
		invitee__exact = invitee,
		created_at__gte = invitation_created_at
	)[0]
	pkgame.status = PKGame.IN_PROGRESS
	pkgame.invitee_init_assets = request.user.profile.assets
	pkgame.save()

def decline_pk(request, invitor, invitee, invitation_created_at):
	# declined, cancel pk
	pkgame = PKGame.objects.filter(
		invitor__exact = invitor,
		invitee__exact = invitee,
		created_at__gte = invitation_created_at
	)[0]
	pkgame.status = PKGame.CANCELED
	pkgame.save()
