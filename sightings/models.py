from django.db import models
from django.utils.translation import gettext as _

class Sightings(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    unique_squirrel_id = models.CharField(max_length=100)
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
    )
    shift = models.CharField(
            max_length=3,
            choices=SHIFT_CHOICES,
            default='AM',
    )
    date=models.DateField('date')
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
    )
    age=models.CharField(
            max_length=10,
            choices=AGE_CHOICES,
            default='',
    )
    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    FUR_CHOICES = (
            (GRAY, 'Gray'),
            (BLACK, 'Black'),
            (CINNAMON, 'Cinnamon'),
    )
    primary_fur_color=models.CharField(
            max_length=10,
            choices=FUR_CHOICES,
            default='',
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOC_CHOICES = (
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
    )
    location=models.CharField(
            max_length=20,
            choices=LOC_CHOICES,
            default='',
    )

    specific_location=models.CharField(max_length=100,default='')

    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    other_activities=models.CharField(max_length=100)
    kuks=models.BooleanField()
    quaas=models.BooleanField()
    moans=models.BooleanField()
    tail_flags=models.BooleanField()
    tail_twitches=models.BooleanField()
    approaches=models.BooleanField()
    indifferent=models.BooleanField()
    runs_from=models.BooleanField()

    def __str__(self):
        return self.unique_squirrel_id
