# Generated by Django 4.2.6 on 2023-12-20 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelViewer', '0006_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
