from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .database import *


def person(request, pk):
	data = select_user_skills(pk)
	responseData = {
        'URIs': data,
    }
	return JsonResponse(data, safe=False)



def index(request):
	return HttpResponse(1)


# Create your views here.
