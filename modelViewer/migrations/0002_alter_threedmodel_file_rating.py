# Generated by Django 4.2.6 on 2023-11-19 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelViewer.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelViewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threedmodel',
            name='file',
            field=models.FileField(help_text='Please use only .glb or .gltf file', upload_to='3dmodels/', validators=[modelViewer.models.validate_gltf_file]),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelViewer.threedmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'model')},
            },
        ),
    ]
