# Generated by Django 4.1 on 2022-08-11 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inv", "0002_subcategoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
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
                        help_text="Descripción de la marca", max_length=100, unique=True
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
            options={"verbose_name_plural": "Marca",},
        ),
        migrations.CreateModel(
            name="UnidadMedida",
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
                        help_text="Descripción de la medida",
                        max_length=100,
                        unique=True,
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
            options={"verbose_name_plural": "Unidades de Medida",},
        ),
        migrations.CreateModel(
            name="Producto",
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
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("codigo_barra", models.CharField(max_length=50)),
                ("descripcion", models.CharField(max_length=200)),
                ("precio", models.FloatField(default=0)),
                ("existencia", models.IntegerField(default=0)),
                ("ultima_compra", models.DateField(blank=True, null=True)),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inv.marca"
                    ),
                ),
                (
                    "subcategoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inv.subcategoria",
                    ),
                ),
                (
                    "unidad_medidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inv.unidadmedida",
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
                "verbose_name_plural": "Productos",
                "unique_together": {("codigo", "codigo_barra")},
            },
        ),
    ]
