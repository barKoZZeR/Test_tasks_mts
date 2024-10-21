from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import InverseSerializer
import random


@swagger_auto_schema(method='post', request_body=InverseSerializer)
@api_view(['POST'])
def inverse(request):
    serializer = InverseSerializer(data=request.data)
    if serializer.is_valid():
        reversed_data = {v: k for k, v in serializer.validated_data.items()}
        return Response(reversed_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def unstable(request):
    if random.choice([True, False]):
        return Response({"message": "HAPPY"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "UNHAPPY"}, status=status.HTTP_400_BAD_REQUEST)