from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
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
        
        
        
class AddTaskForm(forms.ModelForm) :
    
    class Meta :
        
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'project']
        
        
        
class UpdateProjectForm(forms.ModelForm) :
    
    class Meta :
        
        model = Project
        fields = ['title', 'duration', 'description', 'start_date', 'end_date', 'status']
        
        
        
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
    