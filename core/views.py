from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Club, Evenement, EtudiantInscription
from .forms import EtudiantInscriptionForm, InterestsForm
from .ai_utils import recommend_events

def home(request):
    events = Evenement.objects.filter(date_debut__gte=timezone.now()).order_by("date_debut")
    return render(request, "core/home.html", {"events": events})

def clubs_list(request):
    clubs = Club.objects.all().order_by("nom")
    return render(request, "core/clubs_list.html", {"clubs": clubs})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    events = club.evenements.all().order_by("date_debut")
    return render(request, "core/club_detail.html", {"club": club, "events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Evenement, id=event_id)
    remaining = max(event.capacite_max - event.inscriptions.count(), 0)
    return render(request, "core/event_detail.html", {"event": event, "remaining": remaining})

def event_register(request, event_id):
    event = get_object_or_404(Evenement, id=event_id)
    remaining = event.capacite_max - event.inscriptions.count()

    if remaining <= 0:
        return render(request, "core/register_full.html", {"event": event})

    if request.method == "POST":
        form = EtudiantInscriptionForm(request.POST)
        if form.is_valid():
            inscription = form.save(commit=False)
            inscription.evenement = event
            inscription.save()
            return render(request, "core/register_success.html", {"event": event})
    else:
        form = EtudiantInscriptionForm()

    return render(request, "core/register_form.html", {"event": event, "form": form, "remaining": remaining})

def recommendations(request):
    form = InterestsForm(request.GET or None)
    recs = []

    if form.is_valid():
        interests = form.cleaned_data["interests"]
        upcoming = Evenement.objects.filter(date_debut__gte=timezone.now()).order_by("date_debut")
        recs = recommend_events(interests, upcoming)

    return render(request, "core/recommendations.html", {"form": form, "recs": recs})
