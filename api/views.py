from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from core.models import *

from .serializers import *


class MonsterViewList(APIView):

    pagination_class = PageNumberPagination

        
    def get(self, request, format=None):
        i_param = request.query_params.get('i', None)
        search_param = request.query_params.get('s', None)
        monsters = Monster.objects.all()

        if search_param:
            monsters = monsters.filter(
                Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
            )

        if i_param:
            monsters = monsters.filter(author__id=i_param)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(monsters, request)
        serializer = MonsterSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
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
        i_param = request.query_params.get('i', None)
        survivors = Survivor.objects.all()

        if search_param:
            survivors = survivors.filter(
                Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
            )

        if i_param:
            survivors = survivors.filter(author__id=i_param)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(survivors, request)
        serializer = SurvivorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

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
    

class UserViewList(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        search_param = request.query_params.get('s', None)
        players = Profile.objects.all()

        if search_param:
            players = players.filter(nickname__icontains=search_param)
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(players, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = ProfileSerializer(player)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = ProfileSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# class SearchView(APIView):
#     pagination_class = PageNumberPagination

#     def get(self, request, format=None):
#         search_param = request.query_params.get('s', None)

#         # Inicialize as queries para ambas as tabelas
#         monsters = Monster.objects.all()
#         survivors = Survivor.objects.all()

#         # Se o parâmetro 's' estiver presente, faça a pesquisa nos campos relevantes
#         if search_param:
#             monsters = monsters.filter(
#                 Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
#             )
#             survivors = survivors.filter(
#                 Q(characteristics__icontains=search_param) | Q(torments__icontains=search_param)
#             )

#         # Serialize os resultados para ambos os modelos
#         monster_serializer = MonsterSerializer(monsters, many=True)
#         survivor_serializer = SurvivorSerializer(survivors, many=True)

#         # Construa o dicionário de resultados
#         # Construa o dicionário de resultados
#         results_dict = {
#             'monsters': monster_serializer.data,
#             'survivors': survivor_serializer.data
#         }

#         # Use o SearchResultsSerializer para serializar o dicionário
#         results_serializer = SearchResultsSerializer(results_dict)

#         # Paginação
#         paginated_results = {
#             'monsters': self.pagination_class.paginate_queryset(results_dict['monsters'], request),
#             'survivors': self.pagination_class.paginate_queryset(results_dict['survivors'], request),
#         }

#         return self.pagination_class.get_paginated_response(paginated_results)




class ApiRootView(APIView):
    def get(self, request, format=None):
        data = {
            'survivor-list': reverse('survivor-list', request=request, format=format),
            'survivor-detail': reverse('survivor-detail', request=request, args=[1], format=format),
            'monster-list': reverse('monster-list', request=request, format=format),
            'monster-detail': reverse('monster-detail', request=request, args=[1], format=format),
            'user-list': reverse('user-list', request=request, format=format),
            'user-detail': reverse('user-detail', request=request, args=[1], format=format),
            # 'search': reverse('search', request=request, format=format),
        }
        return Response(data)
    
