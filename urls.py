from django.urls import path

from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("person/<int:pk>", views.person, name="person"),
]
