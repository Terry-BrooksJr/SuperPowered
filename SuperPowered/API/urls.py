from API.views import HerosView, ModifyHeroView, PublisherListView, ModifyPublisherView, HeroRacesView, ModifyRaceView, RegisterUserAPIView
from django.urls import path

urlpatterns = [
    path('hero/', HerosView.as_view()),
    path('hero/<int:id>', ModifyHeroView.as_view()),
    path('publisher/', PublisherListView.as_view()),
    path('publisher/<int:id>', ModifyPublisherView.as_view()),
    path('race/',HeroRacesView.as_view()),
    path('publisher/<int:id>',ModifyRaceView.as_view()),
    path("users/", RegisterUserAPIView.as_view(),)


]