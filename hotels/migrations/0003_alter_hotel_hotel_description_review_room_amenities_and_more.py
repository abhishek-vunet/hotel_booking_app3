# Generated by Django 5.0.7 on 2024-07-31 11:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_customer_id_customer_id'),
        ('hotels', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reviews', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='customer.customer')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=10)),
                ('room_description', models.TextField(blank=True, max_length=200)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ac', models.BooleanField()),
                ('number_of_beds', models.IntegerField()),
                ('balcony', models.BooleanField()),
                ('flour_num', models.IntegerField()),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amenities', to='hotels.room')),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
