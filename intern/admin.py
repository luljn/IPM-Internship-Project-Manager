from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from intern.models import Member

# Register your models here.



class MemberInline(admin.StackedInline) :
    
    model = Member
    verbose_name_plural = "Utilisateurs"
    
    
    
class UserAdmin(BaseUserAdmin) :
    
    inlines = [MemberInline]
    
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    
