# Generated by Django 2.2.2 on 2019-07-08 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0014_auto_20190626_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nac',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
