from django.contrib import admin
from .models import TissueSensor, SoupSensor, SmellSensor
# Register your models here.


admin.site.register(TissueSensor)
admin.site.register(SoupSensor)
admin.site.register(SmellSensor)
