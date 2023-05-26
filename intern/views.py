from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.



def error404(request, exception) :
    
    return render(request, 'intern/App/404.html', status=404)    
    


class CustomLoginView(LoginView) :
    
    template_name = 'intern/Login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_invalid(self, form) : 
        
        context = self.get_context_data()
        context['form'] = form
        context['error'] = 'Nom d\'utilisateur et/ou mot de passe incorrect(s).'
        return self.render_to_response(context)



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
    
    
    
class AddTaskView(LoginRequiredMixin ,View) :

    template_name = 'intern/App/pages/task_add.html'

    def get(self, request) :

        return render(request, self.template_name)
    
    def post(self, request) : 

        pass
