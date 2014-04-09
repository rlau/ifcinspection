from django.conf.urls import patterns, url

from inspectionapp import views

urlpatterns = patterns('',
	url(r'^/submit$', views.submit, name='submit'),
	url(r'^$', views.index, name='index'),
	url(r'^/review$', views.index, name='review'),
	url(r'^/login$', views.loginpage, name='login'),
	url(r'^/loginauth$', views.user_login, name='loginauth'),
	)