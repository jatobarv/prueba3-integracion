# Generated by Django 2.2.2 on 2019-06-20 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nac',
            field=models.DateTimeField(default=datetime.datetime(
                2019, 6, 20, 12, 53, 46, 957958)),
        ),
    ]
