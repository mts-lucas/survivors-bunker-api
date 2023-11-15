from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('survivors/', SurvivorViewList.as_view(), name='survivor-list'),
    path('survivors/<int:pk>/', SurvivorDetail.as_view(), name='survivor-detail'),
    path('monsters/', MonsterViewList.as_view(), name='monster-list'),
    path('monsters/<int:pk>/', MonsterDetail.as_view(), name='monster-detail'),
    path('users/', UserViewList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('search/', SearchView.as_view(), name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)