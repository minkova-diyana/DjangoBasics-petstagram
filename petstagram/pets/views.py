from django.shortcuts import render


# Create your views here.
def pet_add_page(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details_page(request, username,slug: str):
    return render(request, 'pets/pet-details-page.html')


def pet_edit_page(request, username, slug: str):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete_page(request, username, slug: str):
    return render(request, 'pets/pet-delete-page.html')
