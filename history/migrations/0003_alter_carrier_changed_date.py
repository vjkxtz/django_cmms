# Generated by Django 3.2.5 on 2021-08-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_carrier_changed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='changed_date',
            field=models.DateTimeField(),
        ),
    ]
