from rest_framework.response import Response
from rest_framework.views import APIView
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLString
from energonexus.core.models import EnergyConsumption
from energonexus.core.schema import EnergyConsumptionType

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

    def get(self, request):
        schema = GraphQLSchema(query=EnergyConsumptionType)
        query = """
        query {
          energyConsumptions {
            id
            timestamp
            energyConsumption
          }
        }
        """
        result = schema.execute(query)
        return Response(result.data)

class EnergyConsumptionType(GraphQLObjectType):
    class Meta:
        name = 'EnergyConsumption'
        fields = ('id', 'timestamp', 'energyConsumption')
