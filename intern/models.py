from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

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
    photo = models.ImageField(default='', null=True, verbose_name='photo de profil')
    
    
    
    def __str__(self) :
        
        return f'{self.user.username} : {self.role}'
    
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
    
# @receiver(post_delete, sender=User)
# def delete_user_profile(sender, instance, **kwargs) :
    
#     try : 
        
#         member = instance.member
#         member.delete()
        
#     except Member.DoesNotExist :
        
#         pass
    
# @receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs) :
    
    if created :
        
        subject = 'Bienvenue chez ICCSOFT pour votre stage.'
        message = 'Vous avez été inscrit sur IPM(Intership Project Manager), l\'application web utilisé pour gérer'
        message += '\n les projets de stage chez ICCSOFT. Vos identfiants de connexion sont : '
        message += f'\n Nom d\'utisateur : {instance.username} \n Mot de passe : S3cret1234! '
        message += '\n l\'application est disponible sur : 127.0.0.0.1:8000 '
        message += 'Vous pouvez changez vos informations personnelles sur la page correspondant à votre profil.'
        message += '\n Nous vous souhaitons une bonne période de stage.'
        from_email = 'mbohlulajonathan4@gmail.com' 
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
    