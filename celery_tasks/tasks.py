from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings

from vom_oa.celery import app


from nporder.models import *
import xlwt


# 定义任务函数
@app.task(ignore_result=True)
def send_notification_email(email_title, email_body, email_from, email_list):
    send_mail(email_title, email_body, email_from, email_list)


@app.task(ignore_result=True)
def send_daily_summary_email():

    # 配置邮件内容
    from_email = settings.DEFAULT_FROM_EMAIL
    subject='NP售前订单安装情况汇总'
    content='Dear all,\n 附件为截止目前NP售前订单完成情况，请查收！'
    to_addr=['yin000shi@126.com',
             '17701620880@163.com',]

    # 制作附件
    data=Nporder.objects.values()
    data_title=list(data[0].keys())
    line_len=len(data)
    col_len=len(data_title)

    excel_obj=xlwt.Workbook(encoding='utf-8')
    excel_tab=excel_obj.add_sheet('sheet1')

    for T in range(0,col_len):
        excel_tab.write(0,T,data_title[T])
    for C in range(0,line_len):
        data_line=dict(data[C])
        for L in range(0,col_len):
            data_field=data_title[L]
            data_value=data_line.get(data_field)
            excel_tab.write(C+1,L,data_value)
    excel_obj.save('./NP_sheet.xls')

    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    msg = EmailMultiAlternatives(subject, content, from_email, to_addr)

    msg.content_subtype = "html"

    # 添加附件（可选）
    msg.attach_file('./NP_sheet.xls')

    # 发送
    msg.send()

