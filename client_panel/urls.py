from django.conf.urls import url, include
from django.contrib import admin

from .views import client_pages

urlpatterns = [
    url(r'^$', client_pages.pages_index, name='client_index'),
    url(r'^index/', client_pages.pages_index, name='client_index'),
]
