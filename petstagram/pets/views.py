from django.shortcuts import render, redirect

from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def pet_add_page(request):
    form = PetAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)


def pet_details_page(request, username, slug: str):
    pet = Pet.objects.get(slug=slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit_page(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, slug)

    context = {
        "form": form,
        "pet": pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete_page(request, username, slug: str):
    pet = Pet.objects.get(slug=slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'pet': pet,
        'form': form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
