from django.db import models
from django.contrib.auth.models import AbstractUser


class CarOwner(AbstractUser):
    national_List = (
        ('RU', 'Russian'),
        ('AZ', 'Azerbajan'),
        ('FR', 'France'),
        ('ENG', 'English'),
        ('USA', 'United states'),
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=3, blank=True, null=True, choices=national_List)


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class DriverLicense(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateTimeField()


class Ownership(models.Model):
    owner_car = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()


