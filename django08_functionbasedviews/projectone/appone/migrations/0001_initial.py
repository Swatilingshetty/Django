# Generated by Django 5.0.6 on 2024-06-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productbrandname', models.CharField(max_length=100)),
                ('Productbrandmodel', models.CharField(max_length=100)),
                ('Productbrandcost', models.FloatField()),
            ],
        ),
    ]