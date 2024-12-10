# Generated by Django 5.1.4 on 2024-12-10 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta1', models.PositiveSmallIntegerField()),
                ('pregunta2', models.PositiveSmallIntegerField()),
                ('pregunta3', models.PositiveSmallIntegerField()),
                ('pregunta4', models.PositiveSmallIntegerField()),
                ('pregunta5', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.alumno')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.profesor')),
            ],
            options={
                'unique_together': {('alumno', 'profesor')},
            },
        ),
    ]
