from django.db import models
from account.models import UserProfile


class Nporder(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_no = models.CharField(max_length=20)
    vin = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    direction = models.CharField(choices=(('添加', '添加'), ('删除', '删除')), default='添加', max_length=20)
    is_changed = models.CharField(choices=(('是', '是'), ('否', '否')),default='否',max_length=20)
    is_finished = models.BooleanField(default=False)
    # =======================以下新增
    finish_time = models.DateTimeField(null=True, blank=True)
    # operator=models.CharField(max_length=20)
    model_code = models.CharField(
        choices=(
        ('ES6002', 'ES6002'), ('ES6003', 'ES6003'), ('ES8002', 'ES8002'), ('ES8003', 'ES8003'), ('ES8004', 'ES8004')),
        max_length=20,null=True,blank=True)
    is_combined=models.BooleanField(default=False)
    province=models.CharField(max_length=20,null=True,blank=True)
    material_code=models.CharField(max_length=50,null=True,blank=True)
    has_np_in_vom=models.BooleanField(default=True)
    vinbom_status=models.BooleanField(default=True)


    def __str__(self):
        return self.vin
