"""consult_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import ajax_api_general, ajax_formations, ajax_catalogues, ajax_sessions

urlpatterns = [
    url(r'^$', ajax_api_general.test),
    url(r'^formations/delete/(?P<id>[0-9]+)$', ajax_formations.formations_delete, name='formations_delete'),
    url(r'^catalogues/delete/(?P<id>[0-9]+)$', ajax_catalogues.catalogues_delete, name='catalogues_delete'),
    url(r'^sessions/delete/(?P<id>[0-9]+)$', ajax_sessions.sessions_delete, name='sessions_delete'),
]
