# Generated by Django 4.2.6 on 2023-12-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelViewer', '0007_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
