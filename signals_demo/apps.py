from django.apps import AppConfig


class SignalsDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals_demo'

    def ready(self):
        # Import signals so the @receiver decorators are registered
        import signals_demo.signals  # noqa: F401
