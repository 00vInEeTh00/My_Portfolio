# Generated by Django 5.1.2 on 2024-10-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=350)),
                ('image', models.ImageField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
                ('video', models.FileField(blank=True, upload_to='videos/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
