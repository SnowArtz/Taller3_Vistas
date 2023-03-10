# Generated by Django 4.1.6 on 2023-02-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("variables", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Measurement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField(blank=True, default=None, null=True)),
                ("unit", models.CharField(max_length=50)),
                ("place", models.CharField(max_length=50)),
                ("dateTime", models.DateTimeField(auto_now_add=True)),
                (
                    "variable",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="variables.variable",
                    ),
                ),
            ],
        ),
    ]
