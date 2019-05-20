# Generated by Django 2.0.13 on 2019-05-20 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anunturi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_inchiriere', models.CharField(choices=[('camere', 'inchiriez pe camere'), ('imobil', 'inchiriez un imobil')], default=None, max_length=20)),
                ('localitate', models.CharField(max_length=50)),
                ('zona', models.CharField(max_length=100)),
                ('pret', models.PositiveIntegerField()),
                ('tip_imobil', models.CharField(choices=[('apartament', 'Apartament'), ('casa', 'Casa/Vila')], default=None, max_length=20)),
                ('camere_libere', models.CharField(choices=[('0', '0 camere'), ('1', '1 camera'), ('2', '2 camere'), ('3', '3 camere'), ('4', '4 camere'), ('5+', '5+ camere')], default=None, max_length=20)),
                ('camere_ocupate', models.CharField(choices=[('0', '0 camere'), ('1', '1 camera'), ('2', '2 camere'), ('3', '3 camere'), ('4', '4 camere'), ('5+', '5+ camere')], default=None, max_length=20)),
                ('compartimentare', models.CharField(choices=[('D', 'Decomandat'), ('SD', 'Semidecomandat'), ('A', 'Altceva')], default=None, max_length=20)),
                ('facilitati', multiselectfield.db.fields.MultiSelectField(choices=[('BA', 'Cu balcon'), ('MC', 'Mobilat complet'), ('CT', 'Centrala termica'), ('FR', 'Frigider'), ('AR', 'Aragaz'), ('MS', 'Masina de spalat')], max_length=250)),
                ('descriere_anunt', models.TextField(max_length=250)),
                ('img1', models.ImageField(upload_to='anunturi/')),
                ('img2', models.ImageField(blank=True, upload_to='anunturi/')),
                ('img3', models.ImageField(blank=True, upload_to='anunturi/')),
                ('img4', models.ImageField(blank=True, upload_to='anunturi/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]