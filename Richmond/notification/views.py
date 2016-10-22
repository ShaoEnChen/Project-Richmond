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

			invite_content = Notification.get_invite_pk(yourname, timespan, mode_name)
			Notification.objects.create(
				n_type = Notification.INVITATION,
				n_from = yourname,
				n_to = invitee,
				content = invite_content
			)
			PKGame.objects.create(
				invitor = yourname,
				invitee = invitee,
				invitor_init_assets = request.user.profile.assets,
				mode = mode
			)

	return redirect('/', permanent = True)

def reply_invitation(request):
	if request.method == 'POST' and 'action' in request.POST and 'id' in request.POST:
		notif = Notification.objects.get(id__exact = request.POST['id'])
		notif.set_is_read()
		if request.POST['action'] == '接受':
			accept_pk(request)
			Notification.objects.create(
				n_type = Notification.ALARM,
				n_to = request.user.username,
				content = Notification.get_you_accept_pk(notif.n_from)
			)
		elif request.POST['action'] == '拒絕':
			decline_pk(request)
			Notification.objects.create(
				n_type = Notification.ALARM,
				n_to = request.user.username,
				content = Notification.get_you_decline_pk(notif.n_from)
			)
	return redirect('/', permanent = True)

def accept_pk(request):
	if request.method == 'POST' and 'invitor' in request.POST and 'invitation_created_at' in request.POST:
		# create notification
		yourname = request.user.username
		invitor = request.POST['invitor']
		invitation_created_at = datetime.strptime(request.POST['invitation_created_at'], '%B %d, %Y, %I:%M %p')
		# create msg
		accept_content = Notification.get_invitee_accept_pk(yourname)
		Notification.objects.create(
			n_type = Notification.ALARM,
			n_from = yourname,
			n_to = invitor,
			content = accept_content
		)
		# accepted, start pk
		pkgame = PKGame.objects.filter(
			invitor__exact = invitor,
			invitee__exact = yourname,
			created_at__gte = invitation_created_at
		)[0]
		pkgame.status = PKGame.IN_PROGRESS
		pkgame.invitee_init_assets = request.user.profile.assets
		pkgame.save()

def decline_pk(request):
	if request.method == 'POST' and 'invitor' in request.POST and 'invitation_created_at' in request.POST:
		# create notification
		yourname = request.user.username
		invitor = request.POST['invitor']
		invitation_created_at = datetime.strptime(request.POST['invitation_created_at'], '%B %d, %Y, %I:%M %p')
		# create msg
		decline_content = Notification.get_invitee_decline_pk(yourname)
		Notification.objects.create(
			n_type = Notification.ALARM,
			n_from = yourname,
			n_to = invitor,
			content = decline_content
		)
		# declined, cancel pk
		pkgame = PKGame.objects.filter(
			invitor__exact = invitor,
			invitee__exact = yourname,
			created_at__gte = invitation_created_at
		)[0]
		pkgame.status = PKGame.CANCELED
		pkgame.save()
