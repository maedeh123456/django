from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('posts/',postlistAPIView.as_view(),name='list'),
    #path(r'^(?P<id>[0-9]{1,3})/$',postdetailAPIView.as_view(),name='detailss'),
    url(r'^(?P<id>\d+)/$',postdetailAPIView.as_view(),name='Details'),
    url(r'^delete/(?P<id>\d+)/$',postDestroyAPIView.as_view(),name='Destroy'),
    url(r'^update/(?P<id>\d+)/$',postUpdateAPIView.as_view(),name='Update'),
    url(r'^edit/(?P<id>\d+)/$',postdetailupdateAPIView.as_view(),name='showupdate'),
    url(r'^destroy/(?P<id>\d+)/$',postRetrieveDestroyAPIView.as_view()),
    url(r'^manage/(?P<id>\d+)/$',postRUpdateDestroyAPIView.as_view()),
    path('create/',postcreateAPIView.as_view(),name='Create')
]
