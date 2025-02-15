# Generated by Django 5.1 on 2024-11-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSS', '0016_alter_whyjoinus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='whyjoinus',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyjoinus',
            name='number_1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyjoinus',
            name='number_2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyjoinus',
            name='text_1',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whyjoinus',
            name='text_2',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
