from django.shortcuts import render
from .serializers import DeviceSerializer, DeviceInfoSerializer
from .models import Device
from rest_framework.response import Response


# Create your views here.
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def device_info(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        version = request.data['version']
        platform = request.data['platform']

        try :
            device = Device.objects.create(version = version, platform = platform)
            return Response({'message':'Device Info saved !!', 'status': 1})

        except Exception as ex:
            return Response({'message':ex, 'status': 0})
    else:
        return Response({'message':serializer.errors,'status':0})

@api_view(['POST'])
def get_device_info(request):
    serializer = DeviceInfoSerializer(data = request.data)
    if serializer.is_valid():
        platform = request.data['platform']

        try:
            device = Device.objects.filter(platform = platform).order_by('-version').first()
            data = {
                'id' : device.id,
                'platform' : device.platform,
                'version' : device.version
            }
            return Response({'data' : data, 'status':1 })

        except Exception as ex:
            return Response({'message': ex, 'status': 0})
    else:
        return Response({'message': serializer.errors, 'status': 0})







