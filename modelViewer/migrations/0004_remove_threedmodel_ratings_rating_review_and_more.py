# Generated by Django 4.2.6 on 2023-12-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelViewer', '0003_remove_threedmodel_rating_average_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threedmodel',
            name='ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
