import json
import simplejson

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View, TemplateView

from vom_oa.mixin import LoginRequiredMixin
from .models import Nporder
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
        fields = ['id', 'order_no', 'vin', 'city', 'creator__username', 'create_time', 'is_changed', 'is_finished']
        if request.user.city=='总部':
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
            order = get_object_or_404(Nporder, pk=request.POST['id'])
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
