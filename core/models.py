from django.db import models

class CategorieClub(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Club(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    date_creation = models.DateField()
    categorie = models.ForeignKey(CategorieClub, on_delete=models.SET_NULL, null=True, blank=True)
    responsable_nom = models.CharField(max_length=120)

    def __str__(self):
        return self.nom


class Evenement(models.Model):
    STATUT_CHOICES = [
        ("A_VENIR", "À venir"),
        ("EN_COURS", "En cours"),
        ("TERMINE", "Terminé"),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="evenements")
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    capacite_max = models.PositiveIntegerField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="A_VENIR")

    def __str__(self):
        return self.titre


class EtudiantInscription(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name="inscriptions")
    nom_etudiant = models.CharField(max_length=150)
    email_etudiant = models.EmailField()
    classe = models.CharField(max_length=100)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_etudiant} - {self.evenement.titre}"
