# Generated by Django 4.2.2 on 2023-06-13 14:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("API", "0009_alter_hero_race"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="hero",
            unique_together={("name", "alignment", "gender", "race")},
        ),
    ]
