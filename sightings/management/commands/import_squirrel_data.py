import csv

from django.core.management.base import BaseCommand

from sightings.models import Sightings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open($@) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        for item in data:
            s = Sightings(
                latitude=item['latitude'],
                longitude=item['longitude'],
                unique_squirrel_id=item['unique_squirrel_id'],
                shift=item['shift'],
                date=item['date'],
                age=item['age'],
                primary_fur_color=item['primary_fur_color'],
                location=item['location'],
                specific_location=item['specific_location'],
                running=item['running'],
                chasing=item['chasing'],
                climbing=item['climbing'],
                eating=item['eating'],
                foraging=item['foraging'],
                other_activities=item['other_activities'],
                kuks=item['kuks'],
                quaas=item['quaas'],
                moans=item['moans'],
                tail_flags=item['tail_flags'],
                tail_twitches=item['tail_twitches'],
                approaches=item['approaches'],
                indifferent=item['indifferent'],
                runs_from=item['runs_from'],
            )
            s.save()
