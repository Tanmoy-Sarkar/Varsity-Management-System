# Generated by Django 3.0.6 on 2020-06-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20200605_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1, unique_for_date='date'),
        ),
    ]
