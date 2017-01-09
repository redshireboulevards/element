from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'element.accounts'
    verbose_name = 'Accounts'

    def ready(self):
        from . import signals  # register signals
