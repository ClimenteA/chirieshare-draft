# Generated by Django 2.0.13 on 2019-05-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunturi', '0002_auto_20190520_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anunturi',
            name='tip_imobil',
            field=models.CharField(choices=[('Ap.', 'Apartament'), ('Casa', 'Casa/Vila')], default=None, max_length=20),
        ),
    ]