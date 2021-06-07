# Generated by Django 3.2.2 on 2021-06-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyTrip', '0003_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('tripid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
            ],
        ),
    ]