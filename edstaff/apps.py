
from django.apps import AppConfig



class EdstaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edstaff'

    def ready(self):
        import edstaff.signals
