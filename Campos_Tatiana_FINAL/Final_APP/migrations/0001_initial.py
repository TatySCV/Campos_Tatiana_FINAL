# Generated by Django 4.2.5 on 2023-12-19 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInstitucion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=80)),
                ('telefono', models.IntegerField()),
                ('fechaInscripcion', models.DateField()),
                ('horaInscripcion', models.TimeField()),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.CharField(blank=True, max_length=255)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Final_APP.institucion')),
            ],
        ),
    ]
