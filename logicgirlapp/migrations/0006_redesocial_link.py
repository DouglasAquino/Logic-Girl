# Generated by Django 3.2.5 on 2021-11-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logicgirlapp', '0005_redesocial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redesocial',
            name='link',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Link do perfil'),
        ),
    ]
