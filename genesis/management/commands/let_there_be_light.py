from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.conf import settings
        from django.utils.importlib import import_module
        from django.utils.module_loading import module_has_submodule
        from django.core import management

        for app in settings.INSTALLED_APPS:
            # try to call the bootstrap command on each app and
            # fail silently if it is not present
            try:
                management.call_command('%s_bootstrap' % app)
            except:
                # raise the exception if it is not related to the bootstrap command
                # being absent
                mod = import_module(app)
                if module_has_submodule(mod, 'management.commands.%s_bootstrap' % app):
                    raise
