from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import *
from .forms import *

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
    
    Projects = Project.objects.all()
    Interships = Intership.objects.all()

    return render(request, 'intern/App/pages/project.html', {'Projects' : Projects, 'Interships' : Interships})



@login_required
def tasklist(request) :
    
    Tasks = Task.objects.all()

    return render(request, 'intern/App/pages/taskboard.html', {'Tasks' : Tasks})



class ProfilView(LoginRequiredMixin ,View) :

    template_name = 'intern/App/pages/profile.html'
    Interships = Intership.objects.all()



    def get(self, request) : 

        return render(request, self.template_name, {'Interships' : self.Interships})
    
    def post(self, request) : 

        pass



class DetailledTaskView(LoginRequiredMixin, UpdateView) :

    template_name = 'intern/App/pages/task_detailled.html'
    model = Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy('tasklist')
    
    
    
class AddTaskView(LoginRequiredMixin, CreateView) :

    template_name = 'intern/App/pages/task_add.html'
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('tasklist')
    
    
    
class DeleteTask(LoginRequiredMixin, DeleteView) :
    
    template_name = 'intern/App/pages/task_delete.html'
    model = Task
    success_url = reverse_lazy('tasklist')
    
    
    
def send_welcome_email(request):
    from django.contrib import messages

    user_id = request.GET.get('user_id', '')
    user = User.objects.get(pk=user_id)

    if user:
        
        subject = 'Bienvenue chez ICCSOFT pour votre stage.'
        message = 'Vous avez été inscrit sur IPM(Intership Project Manager), l\'application web utilisé pour gérer'
        message += '\n les projets de stage chez ICCSOFT. Vos identfiants de connexion sont : '
        message += f'\n Nom d\'utisateur : {user.username} \n Mot de passe : S3cret1234! '
        message += '\n l\'application est disponible sur : localhost:8000/ '
        message += 'Vous pouvez changez vos informations personnelles sur la page correspondant à votre profil.'
        message += '\n Nous vous souhaitons une bonne période de stage.'
        from_email = 'mbohlulajonathan4@gmail.com' 
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'Un email avec un lien de connexion a été envoyé à {}.'.format(user.email))

        try:
            obj = User.objects.get(pk=user.pk)
            return redirect(obj)
        except:
            return redirect('/admin')
