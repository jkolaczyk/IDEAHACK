from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.urls import reverse
from .important import *
from django.views.decorators.csrf import csrf_exempt
import requests  
import json

@csrf_exempt
def person(request): #returns information about recommended jobs for a given person
	post = request.body.decode('ascii')
	json_post = json.loads(post)
	pk = json_post['number']
	responseData = get_results_for_person(json_post['number'])
	return JsonResponse(responseData, safe=False)

def suggestions(request): #returns all skills to be suggested when user enters their skills on the app
	return JsonResponse(get_suggestions_arr(), safe=False)
	
@csrf_exempt
def skills(request): #returns information about recommended jobs for a given set of skills
	post = request.body.decode('ascii')
	json_post = json.loads(post)
	skill_names = json_post['skills']
	skills = set()
	for skill in skill_names:
		skills.add(label_transform_sql(skill))
	responseData = get_matches_for_skillsets(skills)
	return JsonResponse(responseData, safe=False)


# Create your views here.
