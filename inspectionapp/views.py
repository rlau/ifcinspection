from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('home')

def submit(request):
	return HttpResponse('test1')

def review(request):
	return HttpResponse('review')