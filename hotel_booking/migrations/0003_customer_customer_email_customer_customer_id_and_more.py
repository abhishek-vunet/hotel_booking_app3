# Generated by Django 5.0.7 on 2024-07-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0002_customer_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='f', max_length=30),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='f', max_length=30),
        ),
    ]
