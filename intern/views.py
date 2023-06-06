from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import DetailView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
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
    
    Projects = Project.objects.all()
    Tasks = Task.objects.all()

    return render(request, 'intern/App/pages/taskboard.html', {'Projects' : Projects,'Tasks' : Tasks})



@login_required
def tasklistEnded(request, id) :
    
    project = Project.objects.get(id=id)
    Tasks = Task.objects.filter(project=project)

    return render(request, 'intern/App/pages/taskboardEnded.html', {'project' : project,'Tasks' : Tasks})



@login_required
def profile_detail_and_update(request) :
    
    Interships = Intership.objects.all()
    user = request.user
    form = UpdateProfileForm(request.POST or None, instance=user)
    
    if request.method == 'POST':
        
        if form.is_valid() :
            
            form.save()
            return redirect('profile')
    
    return render(request, 'intern/App/pages/profile.html', {'Interships' : Interships, 'form' : form})



class ProfilePhotoUpdate(LoginRequiredMixin, UpdateView) :
    
    model = Intern
    template_name = 'intern/App/pages/profile_photo_update.html'
    form_class = UpdatePhotoForm
    success_url = reverse_lazy('profile')



# @login_required
# def profile_photo_update(request) :
    
#     form = UpdatePhotoForm(request.POST)
    
#     if request.method == 'POST':
        
#         if form.is_valid() :
            
#             form = UpdatePhotoForm(request.POST, request.FILES)
#             photo = form.save(commit=False)
#             # set the uploader to the user before saving the model
#             photo.uploader = request.user
#             # now we can save
#             photo.save()
#             return redirect('profile')
    
#     return render(request, 'intern/App/pages/profile_photo_update.html', {'form' : form})



class ChangePasswordView(LoginRequiredMixin, PasswordChangeView) :
    
    template_name = 'intern/App/pages/password_change.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        
        messages.success(self.request, 'Votre mot de passe a été modifié avec succès.')
        return super().form_valid(form)



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
    
    # On definit la methode dispatch, pour pouvoir utiliser l'objet request.
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    # Pour définir le projet de l'utilisateur dynamiquement.
    # (Ici, on recupere l'utilisateur et son projet 'En cours').
    def get_initial(self) :
        
        initial = super(AddTaskView, self).get_initial()
        user = self.request.user # On recupere l'utilisateur actuellement connecté.
        intern = Intern.objects.get(user=user)
        # internship = Intership.objects.get(intern=intern)
        internships = Intership.objects.filter(intern=intern)
        # project = Project.objects.get(internship=internship)
        
        for internship in internships :
            
            if internship.status == 'En cours' :
                
                project = Project.objects.get(internship=internship)
                initial['project'] = project
        
        initial['status'] = 'En attente'
        
        return initial
    
    # Pour rendre le champ de choix du projet invisible.
    def get_form(self, form_class=None) :
        
        form = super().get_form(form_class)
        form.fields['project'].widget = forms.HiddenInput(attrs={'hidden':True})
        form.fields['project'].label = ''
        return form
    
    
    
class DeleteTask(LoginRequiredMixin, DeleteView) :
    
    template_name = 'intern/App/pages/task_delete.html'
    model = Task
    success_url = reverse_lazy('tasklist')
    
    
    
class UpdateProjectView(LoginRequiredMixin, UpdateView) : 
    
    model = Project
    template_name = 'intern/App/pages/project_update.html'
    form_class = UpdateProjectForm
    success_url = reverse_lazy('project')
    
    
    
class DetailledProjectView(LoginRequiredMixin, DetailView) :
    
    model = Project
    template_name = 'intern/App/pages/project_detailled.html'
    
    
    
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
