from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Sightings

def display_map(request):
    context = {
            'map':map,
    }
    return render(request, 'sightings/map.html', context)

def all_squirrels(request):
    squirrels = Sightings.objects.all()
    context = {
            'squirrels':squirrels,
    }
    return render(request, 'sightings/sightings.html', context)

def update_squirrel(request, unique_squirrel_id):
    sighting = Sightings.objects.get(id=unique_squirrel_id)
    if request.method == 'POST':
        # check form data
        form = SightingsForm(request.POST, instance=get)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_suqirrel_id}')
    else:
        form = SightingsForm(instance=sighting)
    context = {
            'form': form,
    }
    return render(request, 'sightings/edit.html', context)

def add_squirrel(request, unique_squirrel_id):
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
