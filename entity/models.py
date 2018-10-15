from django.db import models


class PeopleEntity(models.Model):
    nberCni = models.CharField(max_length=9, unique=True, null=True, blank=True)
    nberRecep = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150, default="John")
    surname = models.CharField(max_length=150, default="Doe")
    birthdate = models.CharField(max_length=10)
    birthPlace = models.CharField(max_length=1000)
    nationality = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=150)
    madePlace = models.CharField(max_length=150, help_text="Lieu où la carte a été établie")
    statut = models.CharField(max_length=50, default="Indisponible")

    def __str__(self):
        return self.nberRecep