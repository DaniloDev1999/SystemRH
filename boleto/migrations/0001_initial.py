# Generated by Django 4.0.4 on 2022-06-23 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(max_length=255)),
                ('codigoCliente', models.CharField(max_length=255)),
            ],
        ),
    ]
