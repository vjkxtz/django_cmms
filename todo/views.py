from django.shortcuts import render

#Class based views

from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Task


class TaskLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')
    


class TaskListView(LoginRequiredMixin ,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name ='todo/task.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(LoginRequiredMixin ,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'

class TaskCreateView(LoginRequiredMixin ,CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'todo/task_create.html'
    success_url = reverse_lazy("task")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(TaskCreateView, self).form_valid(form)

class TaskEditView(LoginRequiredMixin ,UpdateView):
    model = Task 
    template_name = 'todo/task_edit.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("task")

class TaskDeleteView(LoginRequiredMixin ,DeleteView):
    model = Task
    template_name = 'todo/task_deleteconfirm.html'
    success_url = reverse_lazy("task")