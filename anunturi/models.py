from django.db import models
from multiselectfield import MultiSelectField

from django.conf import settings


class Anunturi(models.Model):
    
    inchiriere = (
        ("camere", "inchiriez pe camere"),
        ("imobil", "inchiriez un imobil")
    )
    
    tip_inchiriere = models.CharField(max_length=20, choices=inchiriere, default=None)

    localitate = models.CharField(max_length=50)
    zona = models.CharField(max_length=100)
    pret = models.PositiveIntegerField()

    imobil = (
        ("Ap.", "Apartament"),
        ("Casa", "Casa/Vila")
    )

    tip_imobil = models.CharField(max_length=20, choices=imobil, default=None)

    camere = (
        ("0", "0 camere"),
        ("1", "1 camera"),
        ("2", "2 camere"),
        ("3", "3 camere"),
        ("4", "4 camere"),
        ("5+", "5+ camere")
    )

    camere_libere = models.CharField(max_length=20, choices=camere, default=None)
    camere_ocupate = models.CharField(max_length=20, choices=camere, default=None)

    compart = (
        ("D", "Decomandat"),
        ("SD", "Semidecomandat"),
        ("A", "Altceva")
    )

    compartimentare = models.CharField(max_length=20, choices=compart, default="A")

    facil = (
        ("BA", "Cu balcon"),
        ("MC", "Mobilat complet"),
        ("CT", "Centrala termica"),
        ("FR", "Frigider"),
        ("AR", "Aragaz"),
        ("MS", "Masina de spalat")
    )

    facilitati = MultiSelectField(max_length=250, choices=facil, blank=True, null=True)

    descriere_anunt = models.TextField(max_length=250, blank=True, null=True)
    
    img1 = models.ImageField(upload_to="anunturi/")
    img2 = models.ImageField(upload_to="anunturi/", blank=True)
    img3 = models.ImageField(upload_to="anunturi/", blank=True)
    img4 = models.ImageField(upload_to="anunturi/", blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    published_date = models.DateTimeField(auto_now_add=True)







