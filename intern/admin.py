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
    
    change_form_template = "admin/auth/user/custom_changeform.html"


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if 'object_id' in request.resolver_match.kwargs:
            rq = request.resolver_match.kwargs['object_id']
            user_obj = User.objects.get(pk=rq)
            context.update({
                'user':user_obj,
            })

        return super().render_change_form(request, context, add, change, form_url, obj)
    
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(Member)
admin.site.register(Intern)
admin.site.register(Tutor)
admin.site.register(Intership)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Phase)
admin.site.register(Document)
    