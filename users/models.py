from django.db import models
from django.contrib.auth.models import AbstractUser

# Added more columns to the default User model(table)

class User(AbstractUser):
    
    telefon = models.CharField(max_length=50, blank=True, null=True) 

    SEX = (
        ("M", "Masculin"),
        ("F", "Feminin"),
        ("N", "Nedefinit"),
    )
    
    sex = models.CharField(max_length=1, choices=SEX, default="N")
    varsta = models.PositiveIntegerField(blank=True, null=True)
    ocupatie = models.CharField(max_length=50, blank=True, null=True)

    imagine = models.ImageField(blank=True, null=True, upload_to="utilizatori/")
