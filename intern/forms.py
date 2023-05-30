from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member



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
    