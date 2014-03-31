from django.conf.urls import patterns, url

from inspectionapp import views

urlpatterns = patterns('',
	url(r'^submit$', views.submit, name='submit'),
	url(r'^$', views.index, name='index'),
	url(r'^review$', views.index, name='review'),
	)