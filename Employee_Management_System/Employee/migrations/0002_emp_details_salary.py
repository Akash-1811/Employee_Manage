# Generated by Django 4.1 on 2022-09-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_details',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]