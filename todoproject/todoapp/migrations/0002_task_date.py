# Generated by Django 3.2.16 on 2023-01-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-05-24'),
            preserve_default=False,
        ),
    ]