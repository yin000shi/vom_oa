from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
import time


import os
import django

from nporder.models import Nporder

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vom_oa.settings')
django.setup()

# 创建Celery的对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.task
def send_notification_email(email_title, email_body, email_from, email_list):
    send_mail(email_title, email_body, email_from, email_list)

