# Generated by Django 3.2.5 on 2021-08-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0006_alter_carrier_changed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='greasing',
            field=models.CharField(choices=[('ultra', 'Ultra'), ('premier', 'Premier')], default='premier', max_length=10),
        ),
    ]
