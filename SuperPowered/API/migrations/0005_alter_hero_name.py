# Generated by Django 4.2.2 on 2023-06-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API", "0004_alter_hero_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hero",
            name="name",
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
