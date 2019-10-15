import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.views.generic.base import View


class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'account/login.html')
        else:
            return HttpResponseRedirect(reverse('dashboard'))

    def post(self, request):
        redirect_to = request.GET.get('next', '/')
        login_form = LoginForm(request.POST)
        ret = dict(login_form=login_form)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dashboard'))
                else:
                    ret['msg'] = '用户未激活！'
            else:
                ret['msg'] = '用户名和密码错误！'
        else:
            ret['msg'] = '用户名和密码不能为空！'
        return render(request, 'account/login.html', ret)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('account:login'))


# class DashboardView(View):
#
#     def get(self, request):
#         return render(request, 'dashboard.html')

class RegisterView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            user_form = RegisterForm()
            return render(request, 'account/register.html', {'user_form': user_form})

    def post(self, request):
        res = dict(result=False)
        user_create_form = RegisterForm(request.POST)
        if user_create_form.is_valid():
            new_user = user_create_form.save(commit=False)
            new_user.password = make_password(user_create_form.cleaned_data['password'])
            new_user.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')
