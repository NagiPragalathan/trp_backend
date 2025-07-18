from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    verbose_name = 'Department Management'

    def ready(self):
        import base.admin  # This ensures admin.py is loaded
