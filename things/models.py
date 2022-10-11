from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    # By default blank=False
    things = models.CharField(max_length=30, unique=True)
    # By default unique=False
    name = models.CharField(blank=True, max_length=120,)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
