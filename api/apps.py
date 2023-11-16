from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self, *args, **kwargs) -> None:
        import api.signals 
        super_ready = super().ready(*args, **kwargs)
        return super_ready
