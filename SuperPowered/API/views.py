from django.shortcuts import render
from API.models import Hero, Alignment, Race, Publisher
from rest_framework import generics
from API.serializers import HeroSerializer, PublisherSerializer, RaceSerializer

class HerosView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class ModifyHeroView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Hero.objects.all()
    serializer_class=HeroSerializer
    lookup_field = 'id'

class PublisherListView(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ModifyPublisherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'id'

class HeroRacesView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class ModifyRaceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'id'