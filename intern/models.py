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
