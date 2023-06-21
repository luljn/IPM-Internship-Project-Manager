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
    # page détaillée et de mise à jour de chaque tâche.
    path('tasklist/<int:pk>/', intern.views.DetailledTaskView.as_view(), name='task_detailled'),
    # page d'ajout tâche.
    path('add_task/', intern.views.AddTaskView.as_view(), name='add_task'),
    # page de suppresion d'une tâche.
    path('delete_task/<int:pk>/', intern.views.DeleteTask.as_view(), name='delete_task'),
    # page du profil.                     
    path('profile/', intern.views.profile_detail_and_update, name='profile'),
    # path pour l'envoie du email après inscription d'un stagiaire.
    path("send_email/", intern.views.send_welcome_email, name="send_email"),
    # page de modification des infos d'un projet.
    path('update_project/<int:pk>/', intern.views.UpdateProjectView.as_view(), name='update_project'),
    # page de détaillée de chaque projet.
    path('project/<int:pk>/', intern.views.DetailledProjectView.as_view(), name='project_detailled'),
    # page des tâches terminés ou annulés.                       
    path('tasklist_project_ended/<int:id>/', intern.views.tasklistEnded, name='tasklistEnded'),
    # page de modification de mot de passe.
    path('change_password/', intern.views.ChangePasswordView.as_view(), name='change_password'),
    # page de modification de la photo de profil.
    path('change_photo/<int:pk>/', intern.views.ProfilePhotoUpdate.as_view(), name='change_photo'),
    # page des documents.
    path('documents/', intern.views.documentlist, name='documents'),
    # page d'ajout de document.
    path('add_document/', intern.views.UploadDocumentView.as_view(), name='add_document'),
    # page d'ajout de document (à une tâche).
    path('add_document_to_task/', intern.views.UploadDocumentToTaskView.as_view(), name='add_document_to_task'),
    # page de téléchargement de document.
    path('download_document/<int:pk>/', intern.views.DownloadFileView.as_view(), name='download_document'),
    # page de suppression de document.
    path('delete_document/<int:pk>/', intern.views.DeleteDocument.as_view(), name='delete_document'),
    # page de mise à jour de chaque document.
    path('documents/<int:pk>/', intern.views.UpdateDocumentView.as_view(), name='document_update'),
    # page de téléchargement de la liste des tâches d'un projet en fichier excel.
    path('export_to_excel/<int:id>/', intern.views.export_to_excel, name='export_to_excel'),
    # page de téléchargement de la liste des tâches du projet 'En cours' en fichier excel.
    path('export_to_excel_current_project/', intern.views.export_to_excel_current_project, name='export_to_excel_current_project'),
    # url pour la recherche.
    path('search/', intern.views.search, name='search')
]

handler404 = 'intern.views.error404'

if settings.DEBUG :
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
