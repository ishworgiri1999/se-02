# Generated by Django 2.0.7 on 2021-03-07 14:03

from django.db import migrations, models
import django.db.models.deletion
from Instructor.models import instructor


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instructor','__first__')
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_length', models.IntegerField()),
                ('distributer_present', models.BooleanField()),
                ('wholesaler_present', models.BooleanField()),
                ('holding_cost', models.FloatField()),
                ('backlog_cost', models.FloatField()),
                ('rounds_completed', models.IntegerField()),
                ('starting_inventory', models.IntegerField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instructor.instructor')),
            ],
        ),


    ]
