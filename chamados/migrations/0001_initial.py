# Generated by Django 4.1.1 on 2022-09-24 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chamado",
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
                ("sccd", models.BigIntegerField(default=0)),
                ("titulo", models.TextField()),
                ("descricao", models.TextField(blank=True, null=True)),
                ("cliente", models.CharField(max_length=100)),
                ("dtAbertura", models.DateTimeField(auto_now=True)),
                ("dtVencimento", models.DateTimeField(auto_now=True)),
                ("dtEncaminhamento", models.DateTimeField(auto_now=True)),
                ("severidade", models.PositiveIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Modulo",
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
                ("nome", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Modulo_Cliente",
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
                (
                    "cliente_pk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chamados.cliente",
                    ),
                ),
                (
                    "modulo_pk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chamados.modulo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Analise",
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
                (
                    "chamado_pk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chamados.chamado",
                    ),
                ),
            ],
        ),
    ]