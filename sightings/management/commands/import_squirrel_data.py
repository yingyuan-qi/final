import csv
import datetime

from django.core.management.base import BaseCommand

from sightings.models import Sightings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        for item in data:
            s = Sightings(
                latitude=item['Y'],
                longitude=item['\ufeffX'],
                unique_squirrel_id=item['Unique Squirrel ID'],
                shift=item['Shift'],
                date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4])),
                age=item['Age'],
                primary_fur_color=item['Primary Fur Color'],
                location=item['Location'],
                specific_location=item['Specific Location'],
                running=True if item['Running'].lower()=='true' else False,
                chasing=True if item['Chasing'].lower()=='true' else False,
                climbing=True if item['Climbing'].lower()=='true' else False,
                eating=True if item['Eating'].lower()=='true' else False,
                foraging=True if item['Foraging'].lower()=='true' else False,
                other_activities=item['Other Activities'],
                kuks=True if item['Kuks'].lower()=='true' else False,
                quaas=True if item['Quaas'].lower()=='true' else False,
                moans=True if item['Moans'].lower()=='true' else False,
                tail_flags=True if item['Tail flags'].lower()=='true' else False,
                tail_twitches=True if item['Tail twitches'].lower()=='true' else False,
                approaches=True if item['Approaches'].lower()=='true' else False,
                indifferent=True if item['Indifferent'].lower()=='true' else False,
                runs_from=True if item['Runs from'].lower()=='true' else False,
            )
            s.save()
