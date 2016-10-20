from datetime import datetime
from django.db import models

class PKGame(models.Model):
	# 單挑狀態
	WAITING = 0
	IN_PROGRESS = 1
	CLOSED = 2
	CANCELED = -1
	STATUS = (
		(WAITING, '等待中'),
		(IN_PROGRESS, '進行中'),
		(CLOSED, '已結束'),
		(CANCELED, '已取消')
	)

	# 單挑規則模式
	MODE1 = 1
	MODE2 = 2
	PK_MODE = (
		(MODE1, '績效評比'),
		(MODE2, '模式2')
	)

	invitor = models.CharField(max_length=100)
	invitee = models.CharField(max_length=100)
	invitor_init_assets = models.FloatField(editable = False, default = 300000.0)
	invitee_init_assets = models.FloatField(editable = False, default = 300000.0)
	created_at = models.DateTimeField(default=datetime.now())
	status = models.IntegerField(choices=STATUS, default=WAITING)
	mode = models.IntegerField(choices=PK_MODE, default=MODE1)
	def __str__(self):
		return "%s v.s. %s" % (self.invitor, self.invitee)
