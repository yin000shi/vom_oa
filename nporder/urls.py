from django.contrib import admin
from django.urls import path

from nporder.views import NporderView, NporderListView, NporderCreateView,NporderDeleteView,NporderFinishView,SendEmailView

app_name='nporder'

urlpatterns = [
    path('',NporderView.as_view(),name='nporder_view'),
    path('list/',NporderListView.as_view(),name='nporder_list'),
    path('create/',NporderCreateView.as_view(),name='nporder_create'),
    path('delete/',NporderDeleteView.as_view(),name='nporder_delete'),
    path('finish/',NporderFinishView.as_view(),name='nporder_finish'),
    path('email/',SendEmailView.as_view(),name='send_email'),
]