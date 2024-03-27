from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello Worlds!' to standart output."

    def handle(self, *args, **options):
        self.stdout.write('Hello World!')
