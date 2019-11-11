from django.db import models
from account.models import UserProfile


# Create your models here.
class SelfDrivePoint(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_no = models.CharField(max_length=50)
    order_time = models.DateTimeField(null=True, blank=True)
    phone_no = models.CharField(max_length=20)
    is_installed = models.CharField(choices=(('是', '是'), ('否', '否')),default='是',max_length=20)
    city = models.CharField(max_length=20)
    point = models.CharField(max_length=10)
    is_handovered = models.CharField(choices=(('是', '是'), ('否', '否')),default='否',max_length=20)

    def __str__(self):
        return self.order_no
