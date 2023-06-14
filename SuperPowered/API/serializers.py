from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField, PrimaryKeyRelatedField, EmailField
from API.models import Race, Alignment, Hero, Publisher, User
from django_restql.mixins import DynamicFieldsMixin
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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
    publisher = StringRelatedField(source='publisher.name') 
    class Meta:
        model = Hero
        fields = '__all__'
        
#Serializer to Register User
class RegisterSerializer(ModelSerializer):
    email = EmailField(
    required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField( write_only=True, required=True, validators=[validate_password])
    username = CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    
    class Meta:
        model = User
        fields = ('username', 'password',
            'email')

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        is_superuser=False,
        is_active=True,
        is_staff=False,
        date_joined=pendulum.now()
        )
        user.set_password(validated_data['password'])
        return user