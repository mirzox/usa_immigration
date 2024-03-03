from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Service, AnotherServices, FamilyServices
from .serializers import ServiceSerializer, AnotherServiceSerializer


class ServiceView(APIView):

    def get(self, request):
        services = ServiceSerializer(Service.objects.all(), many=True)
        return Response(services.data)


class AnotherServiceView(APIView):

    def get(self, request):
        services = AnotherServiceSerializer(AnotherServices.objects.all(), many=True)
        return Response(services.data)


class FamilyServiceView(APIView):

    def get(self, request):
        services = AnotherServiceSerializer(FamilyServices.objects.all(), many=True)
        return Response(services.data)
