# Generated by Django 3.0.5 on 2020-04-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercice_type', models.CharField(max_length=30)),
                ('coach', models.CharField(max_length=50)),
                ('content_live', models.ImageField(upload_to='pics')),
                ('is_live', models.BooleanField(default=True)),
            ],
        ),
    ]
