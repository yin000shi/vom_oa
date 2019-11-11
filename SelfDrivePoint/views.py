import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import SelfDrivePoint
from .forms import PointCreateForm

# Create your views here.
from django.views.generic.base import View, TemplateView

from vom_oa.mixin import LoginRequiredMixin
import datetime


class DatetimeEncode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class PointListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'creator__name', 'order_no', 'order_time', 'phone_no', 'is_installed', 'city', 'point',
                  'is_handovered']
        if request.user.city == 'UCS' or request.user.city == 'DO/VOM':
            order_list = SelfDrivePoint.objects.values(*fields)

        else:
            order_list = SelfDrivePoint.objects.values(*fields).filter(city=request.user.city)
        ret = dict(data=list(order_list))
        ret['code'] = 0
        ret['msg'] = ''
        ret['count'] = 1000
        # return render(request,'nporder/point_order_list.html')
        return HttpResponse(json.dumps(ret, cls=DatetimeEncode, ensure_ascii=False), content_type='application/json')


class PointView(LoginRequiredMixin, TemplateView):
    template_name = 'selfdrivepoint/point_order_list.html'


class PointCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict(order_all=SelfDrivePoint.objects.all())
        if 'id' in request.GET and request.GET['id']:
            order = get_object_or_404(SelfDrivePoint, pk=request.GET['id'])
            ret['order'] = order
        return render(request, 'selfdrivepoint/point_order_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            # order = get_object_or_404(Nporder, pk=request.POST['id'])
            SelfDrivePoint.objects.filter(id=request.POST['id']).update(order_no=request.POST['order_no'],
                                                                        create_time=request.POST['create_time'],
                                                                        phone_no=request.POST['phone_no'],
                                                                        city=request.POST['city'],
                                                                        is_installed=request.POST['is_installed'],
                                                                        point=request.POST['point']
                                                                        )
            res['result'] = True
        else:
            # order = SelfDrivePoint()
            order_form = PointCreateForm(request.POST)
            if order_form.is_valid():
                order_form.save()
                res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class PointDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST['id'].split(','))
            SelfDrivePoint.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class PointFinishView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            SelfDrivePoint.objects.filter(id=request.POST['id']).update(is_handovered='是')
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


