# Generated by Django 3.2.23 on 2024-03-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
    ]
