# Generated by Django 2.2.14 on 2020-08-23 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'County',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Postal_Code', models.CharField(blank=True, max_length=12)),
                ('Price', models.IntegerField(default=100)),
                ('County', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.County')),
            ],
            options={
                'verbose_name': 'Towns',
            },
        ),
    ]
