# Generated by Django 2.2 on 2020-09-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0002_auto_20200910_0836'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaCallBacks',
        ),
        migrations.DeleteModel(
            name='MpesaPayment',
        ),
    ]
