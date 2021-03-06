from django.db import models
from django.utils.translation import gettext as _

class Sightings(models.Model):
    latitude = models.FloatField(null=True,)
    longitude = models.FloatField(null=True,)
    unique_squirrel_id = models.CharField(max_length=100, primary_key=True)
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
    )
    shift = models.CharField(
            max_length=3,
            choices=SHIFT_CHOICES,
            default=AM,
            null=True,
    )
    date=models.DateField(null=True, blank=True,)
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
            null=True,
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
            null=True,
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
            null=True,
    )

    specific_location=models.CharField(
            max_length=100,
            default='',
            null=True,
    )

    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    other_activities=models.CharField(max_length=100, default='', null=True,)
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
