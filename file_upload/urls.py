from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.list_screenshots, name='list_screenshots' ),
    url(r'^upload_screenshot$', views.upload_screenshot, name='upload_screenshot' ),
)
