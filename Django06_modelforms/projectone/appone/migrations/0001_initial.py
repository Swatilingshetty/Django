# Generated by Django 5.0.6 on 2024-06-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('coarsename', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('joindate', models.DateField()),
            ],
        ),
    ]