# Generated by Django 3.2.5 on 2021-11-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logicgirlapp', '0013_alter_usuario_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='status',
            field=models.CharField(choices=[('0', 'editando'), ('1', 'revisão'), ('2', 'publicado')], default='editando', max_length=20, verbose_name='Status da Publicação'),
        ),
    ]
