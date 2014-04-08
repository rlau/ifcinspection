from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
import os

def index(request):
	# main inspection form page
	if not request.user.is_authenticated():
		return redirect(loginpage)
	else:
		houses = []
		name = request.user.house.name
		houses.append(request.user.house.abbreviation)
		houses.append(request.user.house.house1)
		houses.append(request.user.house.house2)
		return render(request, 'inspectionapp/inspectionform.html', {'houses':houses, 'name':name})
def loginpage(request):
	return render(request, 'inspectionapp/login.html', {})

def submit(request):
	house = request.user.house
	if request.method =='POST':
		date = request.POST['inspectionDate']
		house_inspected = request.POST['houseinspected']
		alcohol_found = request.POST['alcoholfound']
		if alcohol_found == 'yes':
			os.system("php emailform.php rlau@mit.edu alcohol subject rlau@mit.edu")
			return HttpResponse('Please email rlau@mit.edu with report and details')
		else:
			return HttpResponse('Alcohol not found')
	else:
		return HttpResponse('Something went wrong')

def review(request):
	# to be implemented
	return HttpResponse('review')

def user_login(request):
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