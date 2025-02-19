# Generated by Django 5.1 on 2024-09-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=100)),
                ('system_name', models.CharField(max_length=100)),
                ('site_logo', models.ImageField(upload_to='uploads/')),
                ('favicon', models.FileField(upload_to='uploads/')),
                ('home_slider1', models.ImageField(upload_to='uploads/')),
                ('home_slider2', models.ImageField(upload_to='uploads/')),
                ('home_slider3', models.ImageField(upload_to='uploads/')),
                ('slider1_text', models.CharField(max_length=255)),
                ('slider2_text', models.CharField(max_length=255)),
                ('slider3_text', models.CharField(max_length=255)),
            ],
        ),
    ]
