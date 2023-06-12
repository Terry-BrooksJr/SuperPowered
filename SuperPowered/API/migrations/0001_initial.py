# Generated by Django 4.2.2 on 2023-06-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255)),
            ],
            options={
                "verbose_name": "alignment",
                "verbose_name_plural": "alignment",
                "db_table": "alignment",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255)),
            ],
            options={
                "verbose_name": "race",
                "verbose_name_plural": "race",
                "db_table": "race",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Hero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("X", "Non-Gendered")],
                        default="X",
                        max_length=1,
                    ),
                ),
                ("eye_color", models.CharField(max_length=255)),
                ("hair_color", models.CharField(max_length=255)),
                ("skin_color", models.CharField(max_length=255)),
                ("weight", models.IntegerField()),
                (
                    "alignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="API.alignment"
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="API.race"
                    ),
                ),
            ],
            options={
                "verbose_name": "hero",
                "verbose_name_plural": "heroes",
                "db_table": "hero",
                "ordering": ["name"],
                "unique_together": {("name", "gender", "alignment")},
            },
        ),
    ]
