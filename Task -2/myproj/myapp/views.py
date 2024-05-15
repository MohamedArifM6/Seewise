from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ProductionLog
from .serializers import ProductionLogSerializer

class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer


    def perform_create(self, serializer):
        instance = serializer.save()
        instance.calculate_oee()  
        instance.save()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.calculate_oee()  
        instance.save()  
        return Response(serializer.data, status=status.HTTP_200_OK)

