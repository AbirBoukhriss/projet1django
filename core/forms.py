from django import forms
from .models import EtudiantInscription

class EtudiantInscriptionForm(forms.ModelForm):
    class Meta:
        model = EtudiantInscription
        fields = ["nom_etudiant", "email_etudiant", "classe"]

class InterestsForm(forms.Form):
    interests = forms.CharField(
        label="Centres d’intérêt (mots-clés séparés par des virgules)",
        widget=forms.TextInput(attrs={"placeholder": "ex: python, robotique, sport"})
    )
