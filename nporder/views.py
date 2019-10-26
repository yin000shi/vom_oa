import json
import simplejson

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, send_mass_mail

# Create your views here.
from django.views.generic.base import View, TemplateView

from vom_oa.mixin import LoginRequiredMixin
from .models import Nporder, UserProfile
from .forms import NporderCreateForm

import datetime


class DatetimeEncode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class NporderListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'order_no', 'vin', 'city', 'creator__name', 'create_time', 'is_changed', 'is_finished',
                  'direction', 'finish_time']
        if request.user.city == 'UCS' or 'DO/VOM':
            order_list = Nporder.objects.values(*fields)

        else:
            order_list = Nporder.objects.values(*fields).filter(city=request.user.city)
        ret = dict(data=list(order_list))
        ret['code'] = 0
        ret['msg'] = ''
        ret['count'] = 1000
        # return render(request,'nporder/order_list.html')
        return HttpResponse(json.dumps(ret, cls=DatetimeEncode, ensure_ascii=False), content_type='application/json')


class NporderView(LoginRequiredMixin, TemplateView):
    template_name = 'nporder/order_list.html'


class NporderCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict(order_all=Nporder.objects.all())
        if 'id' in request.GET and request.GET['id']:
            order = get_object_or_404(Nporder, pk=request.GET['id'])
            ret['order'] = order
        return render(request, 'nporder/order_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            # order = get_object_or_404(Nporder, pk=request.POST['id'])
            Nporder.objects.filter(id=request.POST['id']).update(order_no=request.POST['order_no'],
                                                                 vin=request.POST['vin'],
                                                                 city=request.POST['city'],
                                                                 direction=request.POST['direction'])
            res['result'] = True
        else:
            order = Nporder()
            order_form = NporderCreateForm(request.POST, instance=order)
            if order_form.is_valid():
                order_form.save()
                res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class NporderDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            Nporder.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class NporderFinishView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            Nporder.objects.filter(id=request.POST['id']).update(is_finished=True)
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class SendEmailView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            order = Nporder.objects.get(id=request.POST['id'])
            city = order.city
            users = UserProfile.objects.filter(city=city)
            email_list = []
            for user in users:
                email_list.append(user.email)
            email_title = '【NP刷写通知】' + str(order.vin)
            email_body = 'Dear 质量专员：\n 请尽快完成下列车辆的NP刷写工作：\nVIN：{} \n订单号：{}\n刷写方向：{}\n刷写后请在VOM_OA系统中点击完成确认'.format(
                order.vin, order.order_no, order.direction)
            email_from = 'nio_pilot_helper@163.com'
            send_mail(email_title, email_body, email_from, email_list)
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class NporderEditView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict(order_all=Nporder.objects.all())
        if 'id' in request.GET and request.GET['id']:
            order = get_object_or_404(Nporder, pk=request.GET['id'])
            ret['order'] = order
        return render(request, 'nporder/order_edit.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            # order = get_object_or_404(Nporder, pk=request.POST['id'])
            Nporder.objects.filter(id=request.POST['id']).update(order_no=request.POST['order_no'],
                                                                 vin=request.POST['vin'],
                                                                 city=request.POST['city'],
                                                                 direction=request.POST['direction'],
                                                                 model_code=request.POST['model_code'],
                                                                 is_combined=request.POST['is_combined'],
                                                                 material_code=request.POST['material_code'],
                                                                 is_changed=request.POST['is_changed'])
            res['result'] = True
        else:
            order = Nporder()
            order_form = NporderCreateForm(request.POST, instance=order)
            if order_form.is_valid():
                order_form.save()
                res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')