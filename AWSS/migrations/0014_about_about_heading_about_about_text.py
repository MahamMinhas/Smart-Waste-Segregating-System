# Generated by Django 5.1 on 2024-11-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSS', '0013_remove_about_about_heading_remove_about_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_heading',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='about_text',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
