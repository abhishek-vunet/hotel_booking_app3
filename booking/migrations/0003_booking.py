# Generated by Django 5.0.7 on 2024-08-01 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_timing_booking_delete_booking'),
        ('customer', '0006_rename_customer_id_customer_id'),
        ('hotels', '0003_alter_hotel_hotel_description_review_room_amenities_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('booked_from', models.DateField(default='1000-01-01', null=True)),
                ('booked_till', models.DateField(default='1000-01-01', null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='customer.customer')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='hotels.room')),
            ],
        ),
    ]
