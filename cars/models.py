from django.db import models
from django.utils.text import slugify

class Car(models.Model):
    vin_number = models.CharField(max_length=20, primary_key=True, unique=True)
    licence_plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images", default="")
    slug = models.SlugField(default="", blank=True, null=True, unique=True, db_index=True)

    # If the 'slug' field is empty, a slug is created from the 'vin_number' value.
    # The 'slugify' function converts 'vin_number' to a suitable slug format.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.vin_number)
        super().save(*args, **kwargs)

    # This method is used when an instance of the model is represented as a string, returns the 'vin_number' value for that instance.
    def __str__(self):
        return f"{self.vin_number}"

class ImageUploadModel(models.Model):
    image = models.ImageField(upload_to="uploads")