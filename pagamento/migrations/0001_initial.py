# Generated by Django 4.0.4 on 2022-06-23 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagamento', models.IntegerField()),
                ('formaPagamento', models.CharField(max_length=255)),
                ('parcelaPagamento', models.IntegerField()),
                ('bancoPag', models.CharField(max_length=255)),
                ('agenciaPag', models.CharField(max_length=255)),
                ('contaPag', models.CharField(max_length=255)),
            ],
        ),
    ]