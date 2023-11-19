# json_viewer/management/commands/save_json_data.py
from django.core.management.base import BaseCommand
from json_viewer.views import save_json_data

class Command(BaseCommand):
    help = 'Save JSON data to the database'

    def handle(self, *args, **options):
        save_json_data(None)  # Pass None for the request argument
        self.stdout.write(self.style.SUCCESS('JSON data saved successfully'))
