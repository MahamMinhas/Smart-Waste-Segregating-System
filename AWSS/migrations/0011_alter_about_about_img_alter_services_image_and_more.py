# Generated by Django 5.1 on 2024-11-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSS', '0010_settings_pre_loader_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='about_hero',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='contact_hero',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='faq_hero',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='favicon',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='home_slider1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='home_slider2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='home_slider3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='pre_loader_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='preloader_video',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='pricing_hero',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='services_hero',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
