# Generated by Django 2.0.13 on 2019-05-22 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anunturi', '0004_auto_20190521_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colegi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anunt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anunturi.Anunturi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mesaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj_primit', models.CharField(max_length=250)),
                ('mesaj_trimis', models.CharField(max_length=250)),
                ('anunt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anunturi.Anunturi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]