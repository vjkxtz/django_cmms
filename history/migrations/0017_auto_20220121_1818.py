# Generated by Django 3.2.9 on 2022-01-21 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0016_auto_20220121_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='types',
            name='part',
        ),
        migrations.CreateModel(
            name='Sub_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('part', models.CharField(blank=True, choices=[('bearing', 'Bearing'), ('blade', 'Blade'), ('front pickup trolly', 'Front Pickup Trolly'), ('front non pickup trolly', 'Front Non pickup trolly'), ('rear pickup trolly', 'Rear Pickup Trolly'), ('rear non pickup trolly', 'Rear Non pickup trolly'), ('valve', 'Valve'), ('Cylinder', 'Cylinder')], default='Bearing', max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('work_done_date', models.DateField()),
                ('work_done', models.CharField(blank=True, max_length=100, null=True)),
                ('assembly', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='history.types')),
            ],
        ),
        migrations.AlterField(
            model_name='types',
            name='assembly',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='history.part'),
        ),
    ]
