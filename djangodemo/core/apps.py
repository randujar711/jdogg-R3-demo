from django.apps import AppConfig
#configuration but for this (core) specific app 

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
