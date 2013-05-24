import os

from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import Command as CollectstaticCommand
from django.core.management import CommandError


class Command(CollectstaticCommand):
    """
    Make sure the media dir exists before we're running collecstatic.
    """
    def run(self, *args, **options):
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        super(Command, self).run(*args, **options)

