from API.views import (
    HeroRacesView,
    HerosView,
    ModifyHeroView,
    ModifyPublisherView,
    ModifyRaceView,
    PublisherListView,
    RegisterUserAPIView,
)
from django.http import HttpResponseRedirect
from django.urls import path

urlpatterns = [
    path("", lambda r: HttpResponseRedirect("main")),
    path("hero/", HerosView.as_view(), name="main"),
    path("hero/<int:id>", ModifyHeroView.as_view()),
    path("publisher/", PublisherListView.as_view()),
    path("publisher/<int:id>", ModifyPublisherView.as_view()),
    path("race/", HeroRacesView.as_view()),
    path("publisher/<int:id>", ModifyRaceView.as_view()),
    path(
        "users/",
        RegisterUserAPIView.as_view(),
    ),
]
