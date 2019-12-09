import csv
import datetime

from django.core.management.base import BaseCommand

from sightings.models import Sightings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        field_names=[f.name for f in Sightings._meta.fields]
        with open(options['csv_file'],'w',newline='') as fp:
            
            variables:[
                'latitude',
                'longitude',
                'unique_squirrel_id',
                'shift',
                'date',
                'age',
                'primary_fur_color',
                'location',
                'specific_location',
                'running',
                'chasing',
                'climbing',
                'eating',
                'foraging',
                'other_activities',
                'kuks',
                'quaas',
                'moans',
                'tail_flags',
                'tail_twitches',
                'approaches',
                'indifferent',
                'runs_from']
            
            writer = csv.writer(fp)
            writer.writerow(field_names)

            for row in Sightings.objects.all():
                writer.writerow(getattr(row, variable) for variable in field_names)

        self.stdout.write(self.style.SUCCESS('Export CSV Successful'))
