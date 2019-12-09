from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Sightings
from .forms import SightingsForm
from django.db.models import Avg, Max

def display_map(request):
    sightings = Sightings.objects.all()[:50]
    context = {
            'sightings':sightings,
    }
    return render(request, 'sightings/map.html', context)

def all_squirrels(request):
    squirrels = Sightings.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'sightings/sightings.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        # check form data
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingsForm()

    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)

def stats(request):
    stats1=Sightings.objects.filter(primary_fur_color='Gray').count()
    stats2=Sightings.objects.all().aggregate(avg_latitude=Avg('latitude'))
    stats3=Sightings.objects.all().aggregate(max_latitude=Max('latitude'))
    stats4=Sightings.objects.filter(age='Juvenile').count()
    stats5=Sightings.objects.filter(age='Adult').count()
    context={
            'Stat1':stats1,
            'Stat2':stats2,
            'Stat3':stats3,
            'Stat4':stats4,
            'Stat5':stats5,
            }
    return render(request, 'sightings/stats.html', context)

def update_squirrel(request, unique_squirrel_id):
    sighting = Sightings.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        # check form data
        form = SightingsForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingsForm(instance=sighting)
    context = {
            'form': form,
            'unique_squirrel_id':unique_squirrel_id,
    }
    return render(request, 'sightings/edit.html', context)

