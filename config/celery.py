from  __future__  import absolute_import,unicode_literals
import os
from time import timezone

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')

app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Baku')

app.config_from_object(settings, namespace='CELERY')

#!Celery Beat Settings
# app.conf.beat_schedule = {
#     #?If you are sending every 30 secons sending email use this object
#     'send-email-all-users':{
#         'task':'librarian.tasks',
#         'schedule':30.0
#     }
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))