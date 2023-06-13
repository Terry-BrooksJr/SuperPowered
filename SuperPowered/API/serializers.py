from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField, PrimaryKeyRelatedField
from API.models import Race, Alignment, Hero, Publisher
from django_restql.mixins import DynamicFieldsMixin
from icecream import install

install()

class RaceSerializer(ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"

class AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Alignment
        fields = "__all__"

class PublisherSerializer(ModelSerializer):
    class Meta: 
        model = Publisher
        fields = "__all__"

class HeroSerializer(DynamicFieldsMixin, ModelSerializer):
    race = StringRelatedField(source='race.name')
    alignment = StringRelatedField(source='alignment.name')
    # publisher = PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    class Meta:
        model = Hero
        fields = '__all__'
        
