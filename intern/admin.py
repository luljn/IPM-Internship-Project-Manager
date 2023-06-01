from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from intern.models import *
from .forms import UserProfileForm

# Register your models here.



class MemberInline(admin.StackedInline) :
    
    model = Member
    verbose_name_plural = "Utilisateurs"
    
    
    
class UserAdmin(BaseUserAdmin) :
    
    # form = UserProfileForm
    # add_form = UserProfileForm

    # fieldsets = (
    #     (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'password1', 'password2'),
    #     }),
    # )

    # list_display = ('username', 'email', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # search_fields = ('username', 'email')
    # ordering = ('username',)
    
    inlines = [MemberInline]
    
    
    
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Member)
admin.site.register(Intern)
admin.site.register(Tutor)
admin.site.register(Intership)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Phase)
admin.site.register(Document)
    