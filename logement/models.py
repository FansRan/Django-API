from django.db import models


class Commune(models.Model):
    nom_commune = models.CharField(max_length=45)
    distance_agence = models.FloatField()
    nbre_habitant = models.IntegerField()

    def __str__(self):
        return self.nom_commune


class TypeLogement(models.Model):
    type_logement = models.CharField(max_length=25, primary_key=True)
    charges_forfaitaires = models.FloatField()

    def __str__(self):
        return self.type_logement


class Quartier(models.Model):
    id_commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    libelle_quartier = models.CharField(max_length=35)

    def __str__(self):
        return self.libelle_quartier


class Logement(models.Model):
    type_logement = models.ForeignKey(TypeLogement, on_delete=models.CASCADE)
    id_quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    no = models.CharField(max_length=5)
    rue = models.CharField(max_length=60)
    superficie = models.FloatField()
    loyer = models.FloatField()

    def __str__(self):
        return self.no + "-" + self.rue


class Individu(models.Model):
    num_logement = models.ForeignKey(Logement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField()
    num_telephone = models.CharField(max_length=12)

    def __str__(self):
        return self.nom + " " + self.prenom