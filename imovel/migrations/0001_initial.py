# Generated by Django 4.0.4 on 2022-06-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('valor_imo', models.IntegerField()),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=255)),
                ('tamanho', models.CharField(max_length=255)),
                ('comodos', models.CharField(max_length=255)),
                ('garagem', models.CharField(max_length=255)),
                ('tipoImovel', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
            ],
        ),
    ]
