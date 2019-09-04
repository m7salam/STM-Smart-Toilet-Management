from django.db import models
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Tissuesensor(models.Model):

    owner = models.ForeignKey(Company, on_delete=models.CASCADE, default="1")
    title = models.CharField(max_length=255, blank=True, null=True)
    initial_reading = models.CharField(max_length=255, default="3")
    empty_reading = models.CharField(max_length=255, default="10")
    level_tissuesensor = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        db_table = 'TissueSensor'

    def __str__(self):
        return self.title



class Smellsensor(models.Model):

    owner = models.ForeignKey(Company, on_delete=models.CASCADE, default="1")
    title = models.CharField(max_length=255, blank=True, null=True)
    level_smellsensor = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'SmellSensor'

    def __str__(self):
        return self.title


class Soapsensor(models.Model):

    owner = models.ForeignKey(Company, on_delete=models.CASCADE, default="1")
    title = models.CharField(max_length=255, blank=True, null=True)
    initial_reading = models.CharField(max_length=255, default="4")
    empty_reading = models.CharField(max_length=255, default="12")
    level_soapsensor = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SoapSensor'

    def __str__(self):
        return self.title
