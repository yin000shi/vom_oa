from django.db import models
from account.models import UserProfile


class Nporder(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    order_no = models.CharField(max_length=20, verbose_name='订单号')
    vin = models.CharField(max_length=20, verbose_name='VIN')
    city = models.CharField(max_length=10, verbose_name='城市')
    direction = models.CharField(choices=(('基础版', '基础版'), ('增强版', '增强版'), ('完整版', '完整版')), default='添加', max_length=20,
                                 verbose_name='包名称')
    is_changed = models.CharField(choices=(('是', '是'), ('否', '否')), default='是', max_length=20, verbose_name='线上是否更新')
    is_finished = models.CharField(default='否', choices=(('是', '是'), ('否', '否')), max_length=20, verbose_name='是否完成')
    # =======================以下新增
    internal_order_no = models.CharField(max_length=20, verbose_name='内部单号', null=True,default="")
    applicant = models.CharField(max_length=20, null=True, verbose_name='申请者')
    finish_time = models.DateTimeField(null=True, blank=True, verbose_name='完成时间')
    comment = models.TextField(verbose_name='备注', null=True)
    # operator=models.CharField(max_length=20)
    # model_code = models.CharField(
    #     choices=(
    #         ('ES6002', 'ES6002'), ('ES6003', 'ES6003'), ('ES8002', 'ES8002'), ('ES8003', 'ES8003'),
    #         ('ES8004', 'ES8004')),
    #     max_length=20, null=True, blank=True)
    # is_combined = models.BooleanField(default=False)
    # province = models.CharField(max_length=20, null=True, blank=True)
    # material_code = models.CharField(max_length=50, null=True, blank=True)
    # has_np_in_vom = models.BooleanField(default=True)
    # vinbom_status = models.BooleanField(default=True)

    def __str__(self):
        return self.vin
