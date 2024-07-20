from rest_framework.response import Response
from rest_framework.views import APIView
from energonexus.core.models import EnergyConsumption
from energonexus.core.serializers import EnergyConsumptionSerializer

class EnergyConsumptionView(APIView):
    def get(self, request):
        energy_data = EnergyConsumption.objects.all()
        serializer = EnergyConsumptionSerializer(energy_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnergyConsumptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
       return Response(serializer.errors, status=400)
