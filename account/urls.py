from django.contrib import admin
from django.urls import path,include

from account.views import LoginView,LogoutView,RegisterView


app_name='account'

urlpatterns = [
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
]