# Generated by Django 5.1 on 2024-11-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSS', '0008_settings_facebook_settings_pinterest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='instagram',
            field=models.CharField(default='instagram', max_length=255),
            preserve_default=False,
        ),
    ]
