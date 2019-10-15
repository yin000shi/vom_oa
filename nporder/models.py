from django.db import models
from account.models import UserProfile


class Nporder(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_no = models.CharField(max_length=20)
    vin = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    direction = models.CharField(choices=(('add', '添加'), ('delete', '删除')), default='add', max_length=20)
    is_changed = models.BooleanField(default=True)
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.vin
