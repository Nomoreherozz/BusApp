from django.core.management.base import BaseCommand
from tracker.models import Station, Bus
import json

class Command(BaseCommand):
    help = 'Load Stations'

    def handle(self, *args, **options) -> str | None:
        b = Bus(route=55, plate="61F2-12345", in_stop_id=10, velocity=0.0, distance_from_src=0.0)
        b.run()
