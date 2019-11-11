from django.contrib import admin
from django.urls import path

from SelfDrivePoint.views import *

app_name='selfdrivepoint'

urlpatterns = [
    path('',PointView.as_view(),name='point_view'),
    path('list/',PointListView.as_view(),name='point_list_view'),
    path('create/',PointCreateView.as_view(),name='point_create_view'),
    path('delete/',PointDeleteView.as_view(),name='point_delete'),
    path('finish/',PointFinishView.as_view(),name='point_finish'),
]