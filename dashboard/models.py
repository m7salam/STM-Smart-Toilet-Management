from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class TissueSensor(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    initial_reading = models.CharField(max_length=255, default="3")
    empty_reading = models.CharField(max_length=255, default="8")
    level_tissuesensor = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'TissueSensor'

    def __str__(self):
        return self.title


class SmellSensor(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    level_smellsensor = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SmellSensor'

    def __str__(self):
        return self.title


class SoupSensor(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    initial_reading = models.CharField(max_length=255, default="4")
    empty_reading = models.CharField(max_length=255, default="12")
    level_soupsensor = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SoupSensor'


    def __str__(self):
        return self.title
