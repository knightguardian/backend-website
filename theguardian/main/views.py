from django.shortcuts import render
from django.http import HttpResponse
from . import models

def homepage(request):
	m=models.DbModel(name='as',email="email",password="as")
	m.save()
	return HttpResponse("hello nice to meet you")