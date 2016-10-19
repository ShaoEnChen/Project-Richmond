from django.shortcuts import render, redirect
from .models import Notification

def notification_view(request):
	me = request.user.username
	notif_list = Notification.objects.filter(n_to__exact = me).filter(is_read__exact = False).order_by('-created_at')
	return render(request, 'account/notifications.html', {
		'NOTIF_TYPE': dict(Notification.NOTIF_TYPE),
		'notif_list': notif_list
	})

def invite_pk(request):
	yourname = request.user.username
	invitee = request.GET.get('invitee', '')
	invite_content = Notification.get_invite_pk_content(yourname)
	Notification.objects.create(n_type = Notification.INVITATION, n_from = yourname, n_to = invitee, content = invite_content)
	return redirect('/userList', permanent = True)

# def confirm_pk(request):
