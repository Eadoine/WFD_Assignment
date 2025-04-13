from django.contrib import admin
from .models import Job, AdminActivityLog

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        action = 'Updated' if change else 'Created'
        super().save_model(request, obj, form, change)
        AdminActivityLog.objects.create(
            admin_user=request.user,
            action=f"{action} job",
            description=f"{obj.title} job has been {action.lower()} by {request.user.username}."
        )

    def delete_model(self, request, obj):
        AdminActivityLog.objects.create(
            admin_user=request.user,
            action="Deleted job",
            description=f"{obj.title} job has been deleted by {request.user.username}."
        )
        super().delete_model(request, obj)


# Register your models here.
