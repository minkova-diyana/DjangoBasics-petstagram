from django.shortcuts import render

from petstagram.photos.models import Photo
# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)

def like_functionality(request):
    return render(request, '')