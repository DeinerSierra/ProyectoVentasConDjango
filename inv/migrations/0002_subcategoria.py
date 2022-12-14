# Generated by Django 4.1 on 2022-08-11 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inv", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubCategoria",
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
                ("estado", models.BooleanField(default=True)),
                ("fechaCreacion", models.DateTimeField(auto_now_add=True)),
                ("fechaModificacion", models.DateTimeField(auto_now_add=True)),
                ("usuarioModificador", models.IntegerField(blank=True, null=True)),
                (
                    "descripcion",
                    models.CharField(
                        help_text="Descripción de la categoria", max_length=100
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inv.categoria"
                    ),
                ),
                (
                    "usuarioCreador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Sub Categorias",
                "unique_together": {("categoria", "descripcion")},
            },
        ),
    ]
