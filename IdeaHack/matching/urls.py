from django.urls import path

from . import views
 
urlpatterns = [
    path("person", views.person, name="person"),
    path("suggestions", views.suggestions, name="suggestions"), 
    path("skills", views.skills, name="skills")
]
