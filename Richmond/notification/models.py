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
	n_from = models.CharField(max_length=100)
	n_to = models.CharField(max_length=100)
	content = models.CharField(max_length=2000)
	created_at = models.DateTimeField(default=datetime.now())
	is_read = models.BooleanField(default=False)
	def __str__(self):
		return "%s to %s" % (self.n_from, self.n_to)

	def set_is_read(self):
		self.is_read = True
		self.save()

	# type: INVITATION
	def get_invite_pk_content(m_from, timespan, mode):
		INVITE_TO_PK = '[鐵籠格鬥] ' + m_from + '邀請您與他進行為期' + timespan + '週的' + mode + '單挑！'
		return INVITE_TO_PK

	# type: ALARM
	def get_accept_pk_content(m_from):
		ACCEPT_TO_PK = '[鐵籠格鬥] ' + m_from + '已接受您的單挑邀請'
		return ACCEPT_TO_PK

	# type: ALARM
	def get_decline_pk_content(m_from):
		DECLINE_TO_PK = '[鐵籠格鬥] ' + m_from + '拒絕了您的單挑邀請'
		return DECLINE_TO_PK