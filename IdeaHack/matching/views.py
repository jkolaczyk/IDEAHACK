from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.urls import reverse
from .important import *
from django.views.decorators.csrf import csrf_exempt
import requests  
import json

@csrf_exempt
def person(request):
	post = request.body.decode('ascii')
	json_post = json.loads(post)
	pk = json_post['number']
	responseData = get_results_for_person(json_post['number'])
	return JsonResponse(responseData, safe=False)

def suggestions(request):
	return JsonResponse(get_suggestions_arr(), safe=False)
	
@csrf_exempt
def skills(request):
	post = request.body.decode('ascii')
	json_post = json.loads(post)
	skill_names = json_post['skills']
	skills = set()
	for skill in skill_names:
		skills.add(label_transform_sql(skill))
	responseData = get_matches_for_skillsets(skills)
	return JsonResponse(responseData, safe=False)


# Create your views here.
