from django.forms import ModelForm

form .models import Sightings

class SightingsForm(ModelForm):
    class Meta:
        model = Sightings
        fields = '__all__'
