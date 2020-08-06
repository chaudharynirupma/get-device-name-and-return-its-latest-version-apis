from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    version = serializers.FloatField()
    platform = serializers.CharField()

    class Meta:
        model = Device

class DeviceInfoSerializer(serializers.Serializer):

    platform = serializers.CharField()

    class Meta:
        model = Device