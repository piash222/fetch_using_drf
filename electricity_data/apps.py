from django.apps import AppConfig


class ElectricityDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "electricity_data"

    def ready(self):
        from scheduler import updater
        updater.start()
