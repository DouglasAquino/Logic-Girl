# Generated by Django 3.2.5 on 2021-11-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logicgirlapp', '0003_usuario_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Cargo')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cargo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cargos',
            field=models.ManyToManyField(blank=True, to='logicgirlapp.Cargo'),
        ),
    ]
