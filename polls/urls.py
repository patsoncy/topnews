#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
# ]


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]
