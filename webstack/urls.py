# -*- coding: utf-8 -*-
from django.urls import path

from webstack.views import index

urlpatterns = [
    path('', index, name='webstack_index'),
]
