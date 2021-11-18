# Generated by Django 3.2.5 on 2021-11-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logicgirlapp', '0009_auto_20211118_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='capa_secao2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Imagem da Seção 2'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='titulo_secao1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Titulo da Seção 1'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='titulo_secao2',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Titulo da Seção 2'),
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='capa_secao1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Imagem da Seção 1'),
        ),
    ]
