from django.contrib.staticfiles.management.commands.collectstatic import Command as CollectStaticCommand

from ._grunt import start_grunt as execute_grunt

class Command(CollectStaticCommand):

    def handle(self, *args, **options):
        self.start_grunt()
        return super(Command, self).handle(*args, **options)

    def start_grunt(self):
        execute_grunt(self)