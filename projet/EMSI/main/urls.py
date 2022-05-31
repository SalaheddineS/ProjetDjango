from django.urls import path

from . import views

urlpatterns=[
path("b",views.index,name="index"),
path("a",views.index2,name="index2"),
path("",views.vide,name="vide"),
path("<int:id>",views.id,name="id"),
path("<str:name>",views.name,name="name"),
]