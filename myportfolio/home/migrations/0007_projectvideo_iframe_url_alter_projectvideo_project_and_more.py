# Generated by Django 5.1.2 on 2024-11-09 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_project_project_images_projectimage_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectvideo',
            name='iframe_url',
            field=models.URLField(blank=True, max_length=990, null=True),
        ),
        migrations.AlterField(
            model_name='projectvideo',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='home.project'),
        ),
        migrations.AlterField(
            model_name='projectvideo',
            name='video_url',
            field=models.URLField(max_length=990, null=True),
        ),
    ]
