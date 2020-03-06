from django.urls import path
from blog.views import *

urlpatterns = [
    path('list/',list,name='list'),
    path('details/',details,name='detail'),
]
