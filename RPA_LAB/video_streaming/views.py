from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from video_streaming.models import Video
from .serializers import HomeViewSerializer

# Create your views here.

class HomeViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = HomeViewSerializer
    permission_classes = []


class ChargeViewset(APIView):
    def get(self,request,format=None,*args, **kwargs):
        print(request)
        size = self.kwargs.get('size', None)
        length = self.kwargs.get('length', None)
        type = self.kwargs.get('type', None)
        if size < int(500 * 1024 * 8):
            return Response({'price':'12.5$'})
        
        if length > 318:
            return Response({'price':'24.5$'})
        return Response({'price':'20$'})
            

