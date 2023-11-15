from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import *

from .serializers import *


class MonsterViewList(APIView):

    pagination_class = PageNumberPagination

        
    def get(self, request, format=None):
        search_param = request.query_params.get('s', None)
        monsters = Monster.objects.all()

        if search_param:
            monsters = monsters.filter(
                Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
            )
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(monsters, request)
        serializer = MonsterSerializer(result_page, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MonsterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class MonsterDetail(APIView):

    def get_object(self, pk):
        try:
            return Monster.objects.get(pk=pk)
        except Monster.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        monster = self.get_object(pk)
        serializer = MonsterSerializer(monster)
        return Response(serializer.data)


    def patch(self, request, pk, format=None):
        monster = self.get_object(pk)
        serializer = MonsterSerializer(monster, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        monster = self.get_object(pk)
        monster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SurvivorViewList(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        search_param = request.query_params.get('s', None)
        survivors = Survivor.objects.all()

        if search_param:
            survivors = survivors.filter(
                Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
            )
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(survivors, request)
        serializer = SurvivorSerializer(result_page, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurvivorDetail(APIView):

    def get_object(self, pk):
        try:
            return Survivor.objects.get(pk=pk)
        except Survivor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survivor = self.get_object(pk)
        serializer = SurvivorSerializer(survivor)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        survivor = self.get_object(pk)
        serializer = SurvivorSerializer(survivor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        survivor = self.get_object(pk)
        survivor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
