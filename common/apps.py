from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "common"

    def ready(self):
        from .models import (
            state_city_models,
            category_model,
            order_model,
            banner_model,
        )

        # import management
