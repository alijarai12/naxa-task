from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin



# admin.site.register(Department)

admin.site.register(Profile)

# admin.site.register(Attachment)


class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['department_name']

admin.site.register(Department, DepartmentAdmin)  



class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['project_name', 'owner', 'department', 'completed_status', 'project_start_date', 'project_end_date']
    list_filter = ["completed_status"]
    search_fields = ['project_name']


admin.site.register(Project, ProjectAdmin)  



class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'file_path', 'attachment_date']

admin.site.register(Attachment, AttachmentAdmin)  


