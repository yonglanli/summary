from django.shortcuts import render
from rest_framework import viewsets, filters
from backend.models import KeyWord, KeyWordType
from backend.filters import KeyWordFilter, KeyWordTypeFilter
from django_filters.rest_framework import DjangoFilterBackend
from backend.serializers import KeyWordSerializer, KeyWordListSerializer, KeyWordTypeSerializer
from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    """
        标准的分页器
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 999999
# Create your views here.


class KeyWordViewSet(viewsets.ModelViewSet):
    filter_class = KeyWordFilter
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

    def get_queryset(self):
        return KeyWord.objects.filter(isDelete=False)

    def get_serializer_class(self):
        if self.action == 'list':
            return KeyWordListSerializer
        else:
            return KeyWordSerializer

    def perform_destroy(self, instance):
        instance.isDelete = True
        instance.save()


class KeyWordTypeViewSet(viewsets.ModelViewSet):
    serializer_class = KeyWordTypeSerializer
    filter_class = KeyWordTypeFilter
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

    def get_queryset(self):
        return KeyWordType.objects.filter(isDelete=False)

    def perform_destroy(self, instance):
        instance.isDelete = True
        instance.save()