from django.db import models
from django.utils.translation import gettext_lazy as _


class Race(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    class Meta:
        db_table = "race"
        ordering = ["name"]
        verbose_name = "race"
        verbose_name_plural = "race"

class Alignment(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    class Meta:
        db_table = "alignment"
        ordering = ["name"]
        verbose_name = "alignment"
        verbose_name_plural = "alignment"

class Publisher(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    class Meta:
        db_table = "publisher"
        ordering = ["name"]
        verbose_name = "publisher"
        verbose_name_plural = "publishers"


class Hero(models.Model):
    class GENDER(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        NON_GENDERED = 'X', _('Non-Gendered')        
    
    name = models.CharField(max_length=255, db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER.choices, default=GENDER.NON_GENDERED)
    eye_color = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    hair_color = models.CharField(max_length=255)
    skin_color = models.CharField(max_length=255)
    alignment = models.ForeignKey(Alignment, on_delete=models.PROTECT)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(default="0", null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, default=""),

    class Meta:
        db_table = "hero"
        ordering = ["name"]
        verbose_name = "hero"
        verbose_name_plural = "heroes"
