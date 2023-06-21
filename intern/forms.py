from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *



class LoginForm(forms.Form) :

    username = forms.CharField(max_length=100, label='Nom d\'utilisateur')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Mot de passe')
    
    
    
class UserProfileForm(UserCreationForm) :
    
    email = forms.EmailField()
    
    class Meta : 
        
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
        
    def save(self, commit=True) :
        
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit : 
            
            user.save()
            
        return user    
    
# @receiver(post_save, sender=User)
def save_user_email(sender, instance, created, **kwargs) :
    
    if created :
        
        user = User.objects.get(username=instance.username)
        user.email = instance.email
        user.save()
        
        
       
class UpdateTaskForm(forms.ModelForm) :
    
    class Meta :
        
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'status']
        
        start_date = forms.DateField(required=False)
        end_date = forms.DateField(required=False)
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            # 'description': CKEditorWidget(),
        }
        
        
        
class AddTaskForm(forms.ModelForm) :
    
    class Meta :
        
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'project']
        
        start_date = forms.DateField(required=False)
        end_date = forms.DateField(required=False)
        description = RichTextField()
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': CKEditorWidget(),
        }
        
        
        
class UpdateProjectForm(forms.ModelForm) :
    
    class Meta :
        
        model = Project
        fields = ['description', 'status']
        
        widgets = {
            'description': CKEditorWidget(),
        }
        
        
        
class UpdateProfileForm(forms.ModelForm) :
    
    class Meta :
        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs) :
        
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        
        
        
class UpdatePhotoForm(forms.ModelForm) : 
    
    class Meta :
        
        model = Intern
        fields = ['photo']
        
        
class DocumentUploadForm(forms.ModelForm) :
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DocumentUploadForm, self).__init__(*args, **kwargs)
        
    def CollectUser(self) :
        
        user = self.request.user
        return user
    
    id = 1
    # CHOICES = [('option1', 'Option 1'), ('option2', 'Option 2')]
    # my_choice_field = forms.ChoiceField(choices=CHOICES, widget=forms.Select)
    Tasks = Task.objects.all()
    TASK_CHOICES = [] # liste de choix pour les tâches.
    i = 1
    
    # user = User.objects.get(id=id)
    # intern = Intern.objects.get(user=user)
    # internship = Intership.objects.filter(intern=intern, status='En cours')
    # project = Project.objects.filter(internship=internship, status='En cours')
    # Tasks = Task.objects.all()
    
    # On génère la liste de choix pour les tâches.
    for task in Tasks :
        if task.project.title == "Conception et implémentation d'une application web de suivi des projets de stage" :
            TASK_CHOICES.append((f'option{i}', task))
            i += 1
        
    task = forms.ChoiceField(choices=TASK_CHOICES, widget=forms.Select)
    
    class Meta :
        
        model = Document
        fields = ['title', 'description', 'is_public', 'fichier', 'project', 'phase', 'task']
        # fields = '__all__'
        
        
        
class UpdateDocumentForm(forms.ModelForm) :
    
    class Meta :
        
        model = Document
        fields = ['title', 'description', 'is_public', 'fichier', 'task']
    