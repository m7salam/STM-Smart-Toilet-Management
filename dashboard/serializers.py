from .models import Smellsensor, Tissuesensor, Soapsensor
from rest_framework import serializers

class SmellsensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smellsensor
        fields = ('title', 'level_smellsensor')

class TissuesensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tissuesensor
        fields = ('title', 'level_tissuesensor')


class SoapsensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soapsensor
        fields = ('title', 'level_soapsensor')