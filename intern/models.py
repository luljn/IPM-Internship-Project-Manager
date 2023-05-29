from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.



class Member(models.Model) :
    
    TUTOR = 'Encadreur'
    INTERN = 'Stagiaire'

    ROLES_CHOICES = (
        (TUTOR, 'Encadreur'),
        (INTERN, 'Stagiaire'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, verbose_name='role de l\'utilisateur')
    photo = models.ImageField(null=True, verbose_name='photo de profil')
    
    
    
    def __str__(self) :
        
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs) :
    
    if created :
        
        Member.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs) :
    
    try : 
    
        instance.member.save()
        
    except Member.DoesNotExist : 
        
        pass
    
@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs) :
    
    try : 
        
        member = instance.member
        member.delete()
        
    except Member.DoesNotExist :
        
        pass
    