from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login

def index(request):
	# main inspection form page
	if not request.user.is_authenticated():
		return redirect(loginpage)
	else:
		return render(request, 'inspectionapp/inspectionform.html', {})
def loginpage(request):
	return render(request, 'inspectionapp/login.html', {})

def submit(request):
	# submits form to server.  if no alcohol, goes to thank you page
	# if alcohol, requests email
	return HttpResponse('test1')

def review(request):
	# to be implemented
	return HttpResponse('review')

def user_login(request):
	print 'here'
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Invalid login')
	else:
		return HttpResponse('fail2')