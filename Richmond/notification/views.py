from django.shortcuts import render, redirect
from .models import Notification

def notification_view(request):
	me = request.user.username
	notif_list = Notification.objects.filter(n_to__exact = me).order_by('-created_at')
	try:
		is_empty = notif_list[0]
	except:
		is_empty = None
	return render(request, 'account/notifications.html', {
		'NOTIF_TYPE': dict(Notification.NOTIF_TYPE),
		'notif_list': notif_list,
		'is_empty': is_empty
	})