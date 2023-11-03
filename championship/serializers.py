from rest_framework import serializers
from .models import *


# Serializers define the API representation.
class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = '__all__'