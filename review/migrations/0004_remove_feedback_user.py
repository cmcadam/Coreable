# Generated by Django 2.0.7 on 2018-08-20 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]
