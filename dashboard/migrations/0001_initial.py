# Generated by Django 2.2.4 on 2019-09-11 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tissuesensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('initial_reading', models.CharField(default='3', max_length=255)),
                ('empty_reading', models.CharField(default='10', max_length=255)),
                ('level_tissuesensor', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company')),
            ],
            options={
                'db_table': 'TissueSensor',
            },
        ),
        migrations.CreateModel(
            name='Soapsensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('initial_reading', models.CharField(default='4', max_length=255)),
                ('empty_reading', models.CharField(default='12', max_length=255)),
                ('level_soapsensor', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company')),
            ],
            options={
                'db_table': 'SoapSensor',
            },
        ),
        migrations.CreateModel(
            name='Smellsensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('level_smellsensor', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='dashboard.Company')),
            ],
            options={
                'db_table': 'SmellSensor',
            },
        ),
    ]
