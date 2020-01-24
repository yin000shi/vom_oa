from django.urls import path

from nporder.views import CommentAddView,NporderView, NporderListView, NporderCreateView,NporderDeleteView,NporderFinishView,SendEmailView,NporderEditView

app_name='nporder'

urlpatterns = [
    path('',NporderView.as_view(),name='nporder_view'),
    path('list/',NporderListView.as_view(),name='nporder_list'),
    path('create/',NporderCreateView.as_view(),name='nporder_create'),
    path('edit/', NporderEditView.as_view(), name='nporder_edit'),
    path('delete/',NporderDeleteView.as_view(),name='nporder_delete'),
    path('finish/',NporderFinishView.as_view(),name='nporder_finish'),
    path('email/',SendEmailView.as_view(),name='send_email'),
    path('comment/',CommentAddView.as_view(),name='add_comment'),
]