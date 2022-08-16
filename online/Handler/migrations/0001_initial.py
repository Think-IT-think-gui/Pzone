# Generated by Django 4.0.5 on 2022-08-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name_id', models.CharField(max_length=100)),
                ('Pass_word', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Use_Name', models.CharField(max_length=100)),
                ('Pass_Name', models.CharField(max_length=100)),
                ('Vessel_Name', models.CharField(max_length=100)),
                ('Imo_Number', models.CharField(max_length=100)),
                ('Port_of_Registery', models.CharField(max_length=100)),
                ('Vessel_Type', models.CharField(max_length=100)),
                ('Vessel_Owner', models.CharField(max_length=100)),
                ('Owner_Contact', models.CharField(max_length=100)),
                ('Owner_Email', models.EmailField(max_length=100)),
                ('Vessel_Manager', models.CharField(max_length=100)),
                ('Manager_Contact', models.CharField(max_length=100)),
                ('Manager_Email', models.EmailField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]