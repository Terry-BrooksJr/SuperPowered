from API.models import Alignment, Hero, Publisher, Race, User
from graphene import ObjectType, Schema
from graphene_django import DjangoListField, DjangoObjectType


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
        fields = ( 
            "name",
            "alignment",
            "gender",
            "race",
            "height",
            "weight",
            "skin_color",
            "hair_color",
            "eye_color",
            "publisher")
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'alignment': ['exact', 'icontains', 'istartswith'],
            'gender': ['exact', 'icontains', 'istartswith'],
            'race': ['exact', 'icontains', 'istartswith'],
            'height': ['exact', 'icontains', 'istartswith'],
            'weight': ['exact', 'icontains', 'istartswith'],
            'skin_color': ['exact', 'icontains', 'istartswith'],
            'hair_color': ['exact', 'icontains', 'istartswith'],
            'eye_color': ['exact', 'icontains', 'istartswith'],
            'publisher': ['exact', 'icontains', 'istartswith'],

        }


class RaceType(DjangoObjectType):
    class Meta:
        model = Race
        fields = "__all__"
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
        fields = "__all__"
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }


class AlignmentType(DjangoObjectType):
    class Meta:
        model = Alignment
        fields = "__all__"
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }

class Query(ObjectType):
    heros = DjangoListField(HeroType)
    races = DjangoListField(RaceType)
    alignments = DjangoListField(AlignmentType)

schema = Schema(query=Query)
