from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404

from vom_oa.mixin import LoginRequiredMixin


class DashboardView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'dashboard.html')
