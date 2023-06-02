"""
URL configuration for IPM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

import intern.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # page de connexion.
    path('', intern.views.CustomLoginView.as_view(), name='login'),  
    # page de deconnexion.                                            
    path('logout/', LogoutView.as_view(), name='logout'),  
    # page d'accueil.       
    path('home/', intern.views.home, name='home'),   
    # page du projet.            
    path('project/', intern.views.project, name='project'),  
    # page des tâches des projets 'En cours'.                       
    path('tasklist/', intern.views.tasklist, name='tasklist'),
    # page détaillée de chaque tâche.
    path('tasklist/<int:pk>/', intern.views.DetailledTaskView.as_view(), name='task_detailled'),
    # page d'ajout tâche.
    path('add_task/', intern.views.AddTaskView.as_view(), name='add_task'),
    # page de suppresion d'une tâche.
    path('delete_task/<int:pk>/', intern.views.DeleteTask.as_view(), name='delete_task'),
    # page du profil.                     
    path('profile/', intern.views.ProfilView.as_view(), name='profile'),
    # path pour l'envoie du email après inscription d'un stagiaire.
    path("send_email/", intern.views.send_welcome_email, name="send_email"),
    # page de modification des infos d'un projet.
    path('update_project/<int:pk>/', intern.views.UpdateProjectView.as_view(), name='update_project'),
    # page de détaillée de chaque projet.
    path('project/<int:pk>/', intern.views.DetailledProjectView.as_view(), name='project_detailled'),
    # page des tâches terminés ou annulés.                       
    path('tasklist_project_ended/', intern.views.tasklistEnded, name='tasklistEnded'),
]

handler404 = 'intern.views.error404'

if settings.DEBUG :
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
