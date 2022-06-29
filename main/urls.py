from django.urls import path
from . import views

from .views import TaskList ,TaskDetail,TaskCreate , TaskUpdate , DeleteView ,CustomLoginView , RegisterPage , TaskReorder 
from django.contrib.auth.views import LogoutView


app_name="main"
  
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path('task/', TaskList.as_view(), name='tasks'), 
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'), 
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='main:login'), name='logout'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),
    #path("media/",views.MediaView.as_view(),name="media"),
    path('register/', RegisterPage.as_view(), name='register'), 
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

]
