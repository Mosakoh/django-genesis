from django.core.management.base import BaseCommand

class MyClass(object):
    counter = 0

    @classmethod
    def increment(cls):
        cls.counter += 1


class Command(BaseCommand):
    def handle(self, *args, **options):
        MyClass.increment()
