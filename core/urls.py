from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clubs/", views.clubs_list, name="clubs_list"),
    path("clubs/<int:club_id>/", views.club_detail, name="club_detail"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path("events/<int:event_id>/inscription/", views.event_register, name="event_register"),
    path("recommandations/", views.recommendations, name="recommendations"),
]
