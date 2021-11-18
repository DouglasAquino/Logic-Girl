# Generated by Django 3.2.5 on 2021-11-16 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do usuario')),
                ('bio', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Biografia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500, verbose_name='Titulo da publicação')),
                ('corpo', models.TextField(max_length=15000, verbose_name='Corpo da Publicação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logicgirlapp.usuario')),
            ],
        ),
    ]
