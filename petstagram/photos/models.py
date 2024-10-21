from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ],
        blank=True,
        null=True
    )
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(
        auto_now=True
    )

