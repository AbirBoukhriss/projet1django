from django.contrib import admin
from .models import CategorieClub, Club, Evenement, EtudiantInscription

class EvenementInline(admin.TabularInline):
    model = Evenement
    extra = 0

class InscriptionInline(admin.TabularInline):
    model = EtudiantInscription
    extra = 0

@admin.register(CategorieClub)
class CategorieClubAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "responsable_nom", "date_creation")
    list_filter = ("categorie", "date_creation")
    search_fields = ("nom", "responsable_nom")
    inlines = [EvenementInline]

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ("titre", "club", "statut", "date_debut", "date_fin", "lieu", "capacite_max")
    list_filter = ("club", "statut", "date_debut")
    search_fields = ("titre", "lieu")
    inlines = [InscriptionInline]

@admin.register(EtudiantInscription)
class EtudiantInscriptionAdmin(admin.ModelAdmin):
    list_display = ("nom_etudiant", "email_etudiant", "classe", "evenement", "date_inscription")
    list_filter = ("classe", "evenement")
    search_fields = ("nom_etudiant", "email_etudiant", "classe")
