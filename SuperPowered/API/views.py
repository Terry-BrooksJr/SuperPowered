
from API.custom_renderers import JPEGRenderer, PNGRenderer
from API.models import Alignment, Hero, Publisher, Race
from API.serializers import (
    HeroSerializer,
    PublisherSerializer,
    RaceSerializer,
    RegisterSerializer,
)
from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


# SECTION - Filtering
class HeroFilter(filters.FilterSet):
    class Meta:
        model = Hero
        fields = (
            "id",
            "alignment",
            "publisher",
            "race",
        )


#!SECTION
# SECTION - API Data EndPoints


class HerosView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    filterset_class = HeroFilter
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("name",)


class ModifyHeroView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    renderer_classes = [JPEGRenderer, PNGRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HeroSerializer
    lookup_field = "id"


class PublisherListView(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class ModifyPublisherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PublisherSerializer
    lookup_field = "id"


class HeroRacesView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class ModifyRaceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PublisherSerializer
    lookup_field = "id"


#!SECTION
# SECTION - User Registration Endpoints
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


#!SECTION
