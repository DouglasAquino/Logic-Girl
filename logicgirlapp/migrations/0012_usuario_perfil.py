# Generated by Django 3.2.5 on 2021-11-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logicgirlapp', '0011_publicacao_referencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Url da Imagem para perfil'),
        ),
    ]
