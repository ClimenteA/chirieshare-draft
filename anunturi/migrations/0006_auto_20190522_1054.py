# Generated by Django 2.0.13 on 2019-05-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunturi', '0005_colegi_mesaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesaje',
            name='mesaj_primit',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mesaje',
            name='mesaj_trimis',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
