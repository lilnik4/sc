# Generated by Django 2.1.3 on 2018-12-03 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.CharField(max_length=32),
        ),
    ]
