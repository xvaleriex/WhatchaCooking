from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ("BREAKFAST", "Breakfast"),
    ("LUNCH", "Lunch"),
    ("DINNER", "Dinner"),
    ("SNACK", "Snack"),
]


class Meal(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.FilePathField(path="/img")
    recipe = models.TextField()

