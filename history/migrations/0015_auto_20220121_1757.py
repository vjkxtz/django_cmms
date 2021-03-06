# Generated by Django 3.2.9 on 2022-01-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0014_auto_20220113_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsw_number',
            name='tsw_type',
            field=models.CharField(choices=[('tsw', 'Tsw'), ('retrocate', 'Retrocate')], default='Tsw', max_length=15),
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.CharField(choices=[('carrier', 'Carrier'), ('stop', 'Stop'), ('tsw', 'Tsw'), ('retrocate', 'Retrocate'), ('lift', 'Lift')], default='Carrier', max_length=15)),
                ('part', models.CharField(choices=[('bearing', 'Bearing'), ('blade', 'Blade'), ('pickup trolly', 'Pickup Trolly'), ('non pickup trolly', 'Non pickup trolly'), ('valve', 'Valve'), ('Cylinder', 'Cylinder')], default='Bearing', max_length=20)),
                ('sub_assembly', models.CharField(choices=[('front', 'Front'), ('rear', 'Rear')], default=None, max_length=20)),
                ('line', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='history.linehistory')),
            ],
        ),
    ]
