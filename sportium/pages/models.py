from django.db import models
from multiselectfield import MultiSelectField

GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'), )


PROGRAMS_CHOICES = (
    ('Indoor', 'Indoor Cycling'),
    ('Yoga', 'Yoga'),
    ('Funcional', 'Funcional'),
    ('Hiper', 'Hipertrofia'),
    ('Fat', 'Quema de Grasa'),
    ('Meditacion', 'Meditacion'),
    ('Nutricion', 'Nutricion')
)
# Create your models here.


class LiveVideos(models.Model):

    exercice_type = models.CharField(max_length=30)
    coach = models.CharField(max_length=50)
    videofile = models.FileField(upload_to='videos/', null=True)
    # models.FileField(upload_to='videos/', null=True, verbose_name="")
    content_live = models.ImageField(upload_to='pics', null=True)
    is_live = models.BooleanField(default=True)


class NewCoach(models.Model):

    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    birth = models.DateField(max_length=8, null=True)
    sex = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    profile_pic = models.ImageField(upload_to='pics', null=True)
    classes = MultiSelectField(
        choices=PROGRAMS_CHOICES, max_choices=5, max_length=80, null=True)
