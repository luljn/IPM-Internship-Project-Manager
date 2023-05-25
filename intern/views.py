from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect

# Create your views here.



@login_required
def home(request) :

    return render(request, 'intern/App/index.html')



@login_required
def project(request) :

    return render(request, 'intern/App/pages/project.html')



@login_required
def tasklist(request) :

    return render(request, 'intern/App/pages/taskboard.html')



class ProfilView(LoginRequiredMixin ,View) :

    template_name = 'intern/App/pages/profile.html'



    def get(self, request) : 

        return render(request, self.template_name)
    
    def post(self, request) : 

        pass



class DetailledTaskView(LoginRequiredMixin ,View) :

    template_name = 'intern/App/pages/task_detailled.html'

    def get(self, request) :

        return render(request, self.template_name)
    
    def post(self, request) : 

        pass
