# Generated by Django 2.2.14 on 2020-08-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselhome',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='media/carousel/'),
        ),
    ]
