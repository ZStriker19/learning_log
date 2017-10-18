# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:29:42 2017

@author: zgroves
"""

'''Defines URL patterns for learning_logs'''

from django.conf.urls import url
from . import views

urlpatterns = [
        #Home page
        url(r'^$', views.index, name ='index'),
        #Page displaying all topics
        url(r'^topics/$', views.topics, name='topics'),
        #Detail page for single topic
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        url(r'^new_topic/$', views.new_topic, name='new_topic'),
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
        ]