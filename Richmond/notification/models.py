# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

class Notification(models.Model):
	ALARM = 0
	WARNING = 1
	INVITATION = 2

	NOTIF_TYPE = (
		(ALARM, '系統通知'),
		(WARNING, '警告'),
		(INVITATION, '邀請')
	)

	n_type = models.IntegerField(choices=NOTIF_TYPE, default=ALARM)
	n_from = models.CharField(max_length=100, default='system')
	n_to = models.CharField(max_length=100)
	content = models.CharField(max_length=2000)
	created_at = models.DateTimeField(default=datetime.now())
	is_read = models.BooleanField(default=False)
	def __str__(self):
		return "%s to %s" % (self.n_from, self.n_to)

	def set_is_read(self):
		self.is_read = True
		self.save()

	def get_invite_pk(n_from, timespan, mode):
		content = '[鐵籠格鬥] ' + n_from + '邀請您與他進行為期' + timespan + '週的' + mode + '單挑！'
		return content

	def invitee_pk_response(response, n_from):
		content = '[鐵籠格鬥] ' + n_from + '已' + response + '您的單挑邀請'
		return content

	def your_pk_response(response, n_from):
		content = '[鐵籠格鬥] 您已' + response + n_from + '的單挑邀請'
		return content

