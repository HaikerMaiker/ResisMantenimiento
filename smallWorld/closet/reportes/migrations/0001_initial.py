# Generated by Django 4.2.7 on 2023-11-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('matricula', models.CharField(max_length=9)),
                ('habitacion', models.CharField(max_length=4)),
                ('problema', models.CharField(max_length=1024)),
                ('estatus', models.CharField(default='No resuelto', max_length=20)),
                ('fecha_reporte', models.DateField(auto_now=True)),
            ],
        ),
    ]
