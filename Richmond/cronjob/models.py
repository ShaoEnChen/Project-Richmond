from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models

class Cron_Job_Log(models.Model):
	STATUS_CHOICES = (
	    ('1', _('cron_job_success')),
	    ('2', _('cron_job_failed')),
	)
	title = models.CharField(max_length = 48)
	exec_time = models.DateTimeField(default = timezone.now)
	status_code = models.CharField(max_length = 1, choices = STATUS_CHOICES)
	def __str__(self):
		return self.title
	def success(self):
	    self.status_code = '1'
	def failed(self):
	    self.status_code = '2'