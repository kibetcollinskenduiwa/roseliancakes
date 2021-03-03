# Generated by Django 2.2.14 on 2020-08-23 12:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of this page.', max_length=255, verbose_name='title')),
                ('access_url', models.CharField(help_text='The URL at which this page can be accessed. eg: /terms-and-conditions/', max_length=255, unique=True, verbose_name='access URL')),
                ('redirect_url', models.CharField(blank=True, help_text='The URL to redirect to when this page is accessed.', max_length=255, null=True, verbose_name='redirect URL')),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='The content to be displayed in the body of this page.', null=True, verbose_name='content')),
                ('template_name', models.CharField(choices=[('simple_pages/base.html', 'simple_pages/base.html'), ('simple_pages/default.html', 'simple_pages/default.html'), ('simple_pages/fade.html', 'simple_pages/fade.html'), ('simple_pages/raw.html', 'simple_pages/raw.html')], default='simple_pages/default.html', help_text='The name of the template to use when rendering this page.', max_length=255, verbose_name='template name')),
                ('enabled', models.BooleanField(blank=True, default=True, help_text='If unchecked, this model is disabled.', verbose_name='Enabled')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time on which this model instance was first created.', verbose_name='Created date/time')),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time on which this model instance was last modified.', verbose_name='Modified date/time')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
    ]
