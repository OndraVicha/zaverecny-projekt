# Generated by Django 4.2.6 on 2023-11-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelViewer', '0002_threedmodel_delete_model3d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
