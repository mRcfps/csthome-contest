import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings
from questions.models import Single, Multiple


class Command(BaseCommand):
    help = 'Add single and multiple questions to db'

    def handle(self, *args, **options):
        # Load questions from json
        with open(os.path.join(settings.BASE_DIR, 'fixtures/single.json'), 'r') as fp:
            singles = json.load(fp)
        with open(os.path.join(settings.BASE_DIR, 'fixtures/single.json'), 'r') as fp:
            multiples = json.load(fp)

        for single in singles:
            Single.objects.create(question=single['question'],
                                  answer=single['answer'])

        for multiple in multiples:
            Multiple.objects.create(question=multiple['question'],
                                    answer=multiple['answer'])

        self.stdout.write(self.style.SUCCESS(
            "Successfully add 90 single and 47 multiple questions."
            ))
