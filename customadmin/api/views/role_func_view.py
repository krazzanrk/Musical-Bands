from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from bands.models import Role
from customadmin.api.serializers.role_function_serailizer import RoleSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def role_list(request):
    if request.method == 'GET':
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = RoleSerializer(data=request.data)

        if serializer.is_valid():
            # Role.objects.create(**serializer.validated_data, created_by_id=request.user.id)
            serializer.save(created_by_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk, format=None):
    try:
        role = Role.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = RoleSerializer(role, data=request.data)

        if serializer.is_valid():
            serializer.save(modified_by_id=request.user.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        role.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
