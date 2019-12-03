from django.db import models

# Create your models here.

class Pet(models.Model):

    SEX_CHOICES = [('M','Male'), ('F', 'Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    # using null=True instead of blank=True makes it clear that the age is unknown
    # as apposed to 0 (less than 1)
    age = models.IntegerField(null=True)
    # a pet can have many vaccines
    # and the same vaccine can be applied to many pets
    # so its a many-to-many relationship
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
