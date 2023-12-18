# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment of {self.patient_name} with Dr. {self.name.name}"
