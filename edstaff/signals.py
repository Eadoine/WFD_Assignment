from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Application, Notification


@receiver(post_save, sender=Application)
def send_notification_on_application_update(sender, instance, created, **kwargs):
    if not created:
        # Example: Check if applicant is selected (you can customize this!)
        if hasattr(instance, 'status') and instance.status == 'Selected':
            Notification.objects.create(
                recipient=instance.applicant.user,
                message=f"Congratulations! You have been selected for an interview for the job: {instance.job.title}."
            )
