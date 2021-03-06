# Generated by Django 3.0.5 on 2020-04-23 17:28

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCoach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth', models.DateField(max_length=8)),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, null=True)),
                ('profile_pic', models.ImageField(upload_to='pics/profile_pics')),
                ('classes', multiselectfield.db.fields.MultiSelectField(choices=[('Indoor', 'Indoor Cycling'), ('Yoga', 'Yoga'), ('Funcional', 'Funcional'), ('Hiper', 'Hipertrofia'), ('Fat', 'Quema de Grasa'), ('Meditacion', 'Meditacion'), ('Nutricion', 'Nutricion')], max_length=80)),
            ],
        ),
    ]
