# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Smellsensor(models.Model):
    title = models.CharField(max_length=-1, blank=True, null=True)
    level_smellsensor = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'SmellSensor'


class Soupsensor(models.Model):
    title = models.CharField(max_length=-1, blank=True, null=True)
    initial_reading = models.CharField(max_length=-1, blank=True, null=True)
    empty_reading = models.CharField(max_length=-1, blank=True, null=True)
    level_soupsensor = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'SoupSensor'


class Tissuesensor(models.Model):
    title = models.CharField(max_length=-1, blank=True, null=True)
    initial_reading = models.CharField(max_length=-1, blank=True, null=True)
    empty_reading = models.CharField(max_length=-1, blank=True, null=True)
    level_tissuesensor = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TissueSensor'
