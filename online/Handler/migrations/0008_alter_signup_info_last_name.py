# Generated by Django 4.0.5 on 2022-08-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0007_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_info',
            name='Last_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]