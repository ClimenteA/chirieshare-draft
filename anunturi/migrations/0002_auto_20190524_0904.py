# Generated by Django 2.0.13 on 2019-05-24 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anunturi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chirias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.CharField(blank=True, max_length=250, null=True)),
                ('data_trimiterii', models.DateTimeField(auto_now_add=True)),
                ('anunt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anunturi.Anunturi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.CharField(blank=True, max_length=250, null=True)),
                ('data_trimiterii', models.DateTimeField(auto_now_add=True)),
                ('anunt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anunturi.Anunturi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='colegi',
            name='anunt',
        ),
        migrations.RemoveField(
            model_name='colegi',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mesaje',
            name='anunt',
        ),
        migrations.RemoveField(
            model_name='mesaje',
            name='client',
        ),
        migrations.DeleteModel(
            name='Colegi',
        ),
        migrations.DeleteModel(
            name='Mesaje',
        ),
    ]
