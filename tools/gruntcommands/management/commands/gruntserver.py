from django.contrib.staticfiles.management.commands.runserver import Command as RunServerCommand

from ._grunt import start_grunt as execute_grunt

class Command(RunServerCommand):

    def get_handler(self, *args, **options):
        self.start_grunt()
        return super(Command, self).get_handler(*args, **options)

    def start_grunt(self):
        execute_grunt(self, 'watch')