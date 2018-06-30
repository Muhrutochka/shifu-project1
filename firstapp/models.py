from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Colombina(models.Model):
    context = models.CharField(max_length=301)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=30)