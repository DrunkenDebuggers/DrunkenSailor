from django.contrib import admin
from sailor.models import Project,Label

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    exclude=['creator']
    def save_model(self,request,obj,form,change):
        obj.creator = request.user
        obj.save()

admin.site.register(Project,ProjectAdmin)
admin.site.register(Label)
