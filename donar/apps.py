from django.apps import AppConfig

class DonarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donar'

    def ready(self):
        from .models import user_model  # Importing user_model
        
  
        
