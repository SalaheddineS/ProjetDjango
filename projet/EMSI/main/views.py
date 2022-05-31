from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,items

# Create your views here.

def index(response):
    return HttpResponse("<h1>hey c'est salah </h1>")

def index2(response):
    return HttpResponse("<h1>hey c'est salah22 </h1>")

def vide(response):
    return HttpResponse("<h1>hey c'est la page index vide </h1>")

def id(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.name)   

def name(response,name):
    ls=ToDoList.objects.get(name=name)
    items =ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1>" %(ls.name,items.text)) 