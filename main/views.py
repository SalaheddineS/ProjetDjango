from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView ,FormView

#todo list 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Imports for Reordering Feature
from django.views import View
from django.db import transaction
from .forms import PositionForm

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('main:tasks'))

class CustomLoginView(LoginView):
    template_name="main/login.html"
    fields=['title', 'description', 'complete']
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy("main:tasks")


class RegisterPage(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main:tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name='task' 
    template_name= 'main/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model =  Task
    fields=['title', 'description', 'complete']
    success_url=reverse_lazy("main:tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model =  Task
    fields=['title', 'description', 'complete']
    success_url=reverse_lazy("main:tasks")

class DeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy("main:tasks")




# Create your views here.
class HomeView(TemplateView):
    template_name = "main/index_.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context["test"]="test-1"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context["test"]="test-1"
        return context


class ContactView(TemplateView):
    template_name = "main/contact.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context["test"]="test-1"
        return context
 