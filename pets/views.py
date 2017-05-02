from django.shortcuts import render

from pets.api import Api

def index(request):
    pets_list = Api().master_list()
    context = {'pets_list': pets_list}
    return render(request, 'pets/index.html', context)

def species(request, species_id):
    species = Api().species(species_id)
    context = {'species': species}
    return render(request, 'pets/species.html', context)

def ability(request, ability_id):
    ability = Api().ability(ability_id)
    context = {'ability': ability}
    return render(request, 'pets/ability.html', context)
