from django.shortcuts import render
from notification.models import Notification

def index_view(request):
	return render(request, 'index.html', {
		'notif_num': Notification.objects.filter(n_to = request.user, is_read = False).count()
	})
