# Generated by Django 4.0.5 on 2022-08-09 00:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0010_remove_signup_info_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_info',
            name='Img',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
