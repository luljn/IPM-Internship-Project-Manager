from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser) :

    ADMIN = 'Encadreur'
    INTERN = 'Stagiaire'

    ROLES_CHOICES = (
        (ADMIN, 'Encadreur'),
        (INTERN, 'Stagiaire'),
    )

    user_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant utilisateur')
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, verbose_name='role de l\'utilisateur')
    photo = models.ImageField(verbose_name='photo de profil')
    
    
    
# class Intern(User) :
    
#     role = User.INTERN
#     is_superuser = False
    
    
    
# class Admin(User) :
    
#     role = User.ADMIN
#     is_superuser = True
    
    
    
# class Intership(models.Model) : 
    
#     EN_ATTENTE = 'En attente'
#     EN_COURS = 'En cours'
#     TERMINE = 'Termine'
#     ANNULE = 'Annule'
    
#     STATUS_CHOICES = (
#         (EN_ATTENTE, 'En attente'),
#         (EN_COURS, 'En cours'),
#         (TERMINE, 'Termine'),
#         (ANNULE, 'Annule'),
#     )
    
#     intership_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant stage')
#     duration = models.DurationField(verbose_name="durée du stage")
#     start_date = models.DateField(verbose_name="date de début")
#     end_date = models.DateField(verbose_name="date de fin")
#     status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="statut")
#     user = models.ForeignKey(Intern, on_delete=models.CASCADE)
    
    
    
# class Project(models.Model) :
    
#     EN_ATTENTE = 'En attente'
#     EN_COURS = 'En cours'
#     TERMINE = 'Termine'
#     ANNULE = 'Annule'
    
#     STATUS_CHOICES = (
#         (EN_ATTENTE, 'En attente'),
#         (EN_COURS, 'En cours'),
#         (TERMINE, 'Termine'),
#         (ANNULE, 'Annule'),
#     )
    
#     project_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant projet')
#     title = models.CharField(max_length=500, verbose_name="titre")
#     description = models.CharField(max_length=5500, verbose_name="description")
#     start_date = models.DateField(verbose_name="date de début")
#     end_date = models.DateField(verbose_name="date de fin")
#     status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="statut")
#     internship = models.ForeignKey(Intership, on_delete=models.CASCADE)
    
    
    
# class Task(models.Model) :
    
#     EN_ATTENTE = 'En attente'
#     EN_COURS = 'En cours'
#     TERMINE = 'Termine'
#     ANNULE = 'Annule'
    
#     STATUS_CHOICES = (
#         (EN_ATTENTE, 'En attente'),
#         (EN_COURS, 'En cours'),
#         (TERMINE, 'Termine'),
#         (ANNULE, 'Annule'),
#     )
    
#     task_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant tâche')
#     title = models.CharField(max_length=500, verbose_name="titre")
#     description = models.CharField(max_length=5500, verbose_name="description")
#     start_date = models.DateField(verbose_name="date de début")
#     end_date = models.DateField(verbose_name="date de fin")
#     status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="statut")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    
    
# class Phase(models.Model) :
    
#     EN_ATTENTE = 'En attente'
#     EN_COURS = 'En cours'
#     TERMINE = 'Termine'
#     ANNULE = 'Annule'
    
#     STATUS_CHOICES = (
#         (EN_ATTENTE, 'En attente'),
#         (EN_COURS, 'En cours'),
#         (TERMINE, 'Termine'),
#         (ANNULE, 'Annule'),
#     )
    
#     phase_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant phase')
#     title = models.CharField(max_length=500, verbose_name="titre")
#     description = models.CharField(max_length=5500, verbose_name="description")
#     start_date = models.DateField(verbose_name="date de début")
#     end_date = models.DateField(verbose_name="date de fin")
#     status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name="statut")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    
    
    
# class Document(models.Model) :
    
#     document_id = models.IntegerField(primary_key=True, auto_created=True, db_column='id', verbose_name='identifiant document')
#     title = models.CharField(max_length=500, verbose_name="titre")
#     description = models.CharField(max_length=5500, verbose_name="description")
#     is_public = models.BooleanField(verbose_name="Autorisation de partage")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
    