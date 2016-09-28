from django.utils.translation import ugettext_lazy as _
from django.db import models

class Cron_Job_Log(models.Model):
	STATUS_CHOICES = (
	    ('1', _('cron_job_success')),
	    ('2', _('cron_job_failed')),
	)
	title = models.CharField(max_length=48, default='', verbose_name=_('cronjob_title'))
	exec_time = models.DateTimeField(auto_now_add=True, verbose_name=_('cronjob_exec_time'))
	status_code = models.CharField(default='1', max_length=1, choices=STATUS_CHOICES, verbose_name=_('cronjob_status'))
	def success(self):
	    self.status_code = '1'
	def failed(self):
	    self.status_code = '2'