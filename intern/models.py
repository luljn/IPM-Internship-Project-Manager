from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from ckeditor.fields import RichTextField


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
    
class Intern(models.Model) :
    
    TUTOR = 'Encadreur'
    INTERN = 'Stagiaire'

    ROLES_CHOICES = (
        (INTERN, 'Stagiaire'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, default=INTERN, verbose_name='role de l\'utilisateur')
    photo = models.ImageField(default='defaultUserPicture.png', verbose_name='photo de profil')
    
    class Meta :
        
        verbose_name = "Stagiaire"
        verbose_name_plural = "Stagiaires"
        
    def __str__(self) :
        
        return f'{self.user.first_name} {self.user.last_name}'
    
    
    
class Tutor(models.Model) :
    
    TUTOR = 'Encadreur'
    INTERN = 'Stagiaire'

    ROLES_CHOICES = (
        (TUTOR, 'Encadreur'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, default=TUTOR, verbose_name='role de l\'utilisateur')
    photo = models.ImageField(default='defaultUserPicture.png', verbose_name='photo de profil')
    
    class Meta :
        
        verbose_name = "Encadreur"
        verbose_name_plural = "Encadreurs"
        
    def __str__(self) :
        
        return f'{self.user.first_name} {self.user.last_name}'
    
    
#@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs) :
    
    if created :
        
        Member.objects.create(user=instance)
        
#@receiver(post_save, sender=User)
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
        
        
        
class Intership(models.Model) : 
    
    EN_ATTENTE = 'En attente'
    EN_COURS = 'En cours'
    TERMINE = 'Terminé'
    ANNULE = 'Annulé'
    
    STATUS_CHOICES = (
        (EN_ATTENTE, 'En attente'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        (ANNULE, 'Annulé'),
    )
    
    duration = models.IntegerField(null=True, blank=True, verbose_name="durée du stage(en semaines)")
    start_date = models.DateField(null=True, blank=True, verbose_name="date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="date de fin")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="etat")
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    
    class Meta :
        
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
        
    def clean(self) :
        
        super().clean()

        if self.start_date and self.end_date and self.end_date < self.start_date :
            
            raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")
        
    def __str__(self) :
        
        return f'Stage de {self.intern.user.first_name} {self.intern.user.last_name} - {self.start_date}'
    
    
    
class Project(models.Model) :
    
    EN_ATTENTE = 'En attente'
    EN_COURS = 'En cours'
    TERMINE = 'Terminé'
    ANNULE = 'Annulé'
    
    STATUS_CHOICES = (
        (EN_ATTENTE, 'En attente'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        (ANNULE, 'Annulé'),
    )
    
    title = models.CharField(max_length=500, verbose_name="titre")
    description =  RichTextField(blank=True, null=True, verbose_name="description")
    duration = models.IntegerField(null=True, blank=True, verbose_name="durée du projet(en semaines)")
    start_date = models.DateField(null=True, blank=True, verbose_name="date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="date de fin")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="etat")
    internship = models.ForeignKey(Intership, on_delete=models.CASCADE)
    
    class Meta :
        
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        
    def clean(self) :
        
        super().clean()

        if self.start_date and self.end_date and self.end_date < self.start_date :
            
            raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")
        
    def __str__(self) :
        
        return f'Projet {self.title} - Stagiaire : {self.internship.intern.user.first_name} {self.internship.intern.user.last_name}'
    
    
    
class Task(models.Model) :
    
    EN_ATTENTE = 'En attente'
    EN_COURS = 'En cours'
    TERMINE = 'Terminé'
    ANNULE = 'Annulé'
    
    STATUS_CHOICES = (
        (EN_ATTENTE, 'En attente'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        (ANNULE, 'Annulé'),
    )
    
    title = models.CharField(max_length=500, verbose_name="titre")
    duration = models.IntegerField(null=True, blank=True, verbose_name="durée de la tâche(en jours)")
    description = RichTextField(blank=True, null=True, verbose_name="description")
    start_date = models.DateField(null=True, blank=True, verbose_name="date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="date de fin")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="etat")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    class Meta :
        
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
        
    def clean(self) :
        
        super().clean()

        if self.start_date and self.end_date and self.end_date < self.start_date :
            
            raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")
        
    def __str__(self) :
        
        return f'{self.title}'
        # return f'{self.title}- Projet : {self.project.title}'
    
    
    
class Phase(models.Model) :
    
    EN_ATTENTE = 'En attente'
    EN_COURS = 'En cours'
    TERMINE = 'Terminé'
    ANNULE = 'Annulé'
    
    STATUS_CHOICES = (
        (EN_ATTENTE, 'En attente'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        (ANNULE, 'Annulé'),
    )
    
    title = models.CharField(max_length=500, verbose_name="titre")
    description = RichTextField(blank=True, null=True, verbose_name="description")
    duration = models.IntegerField(null=True, blank=True, verbose_name="durée de la phase(en jours)")
    start_date = models.DateField(null=True, blank=True, verbose_name="date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="date de fin")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="etat")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    class Meta :
        
        verbose_name = "Phase"
        verbose_name_plural = "Phases" 
        
    def clean(self) :
        
        super().clean()

        if self.start_date and self.end_date and self.end_date < self.start_date :
            
            raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")
        
    def __str__(self) :
        
        return f'{self.title} - Projet : {self.project.title}'
    
    
    
class Document(models.Model) :
    
    title = models.CharField(max_length=500, verbose_name="titre")
    description = RichTextField(null=True, blank=True, verbose_name="description")
    is_public = models.BooleanField(default=False, verbose_name="Autorisation de partage")
    fichier = models.FileField(upload_to='documents/')
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL)
    phase = models.ForeignKey(Phase, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta :
        
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        
    def __str__(self) :
        
        if self.project is not None :
            
            return f'{self.title} - Projet : {self.project.title}'
        
        elif self.phase is not None :
            
            return f'{self.title} - Phase : {self.phase.title}'
        
        elif self.task is not None :
            
            return f'{self.title} - Tâche : {self.task.title}'
        
        else  :
            
            return f'{self.title}'
    