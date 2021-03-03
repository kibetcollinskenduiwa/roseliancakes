# Generated by Django 2.2 on 2020-09-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_delivery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clearorders',
            old_name='Name_Other',
            new_name='Name_other',
        ),
        migrations.AlterField(
            model_name='clearorders',
            name='Signature',
            field=models.ImageField(blank=True, upload_to='media/mobile/delivery/signatures'),
        ),
        migrations.AlterField(
            model_name='clearorders',
            name='SystemDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
