from django.shortcuts import render

from apps.magnet.models import Magnet
from apps.magnet.serializers import MagnetSerializers

from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .filter import MagnetFilter

# Create your views here.


class MagnetPagenation(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class MagnetListView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    磁力链接列表
    """
    queryset = Magnet.objects.all()
    serializer_class = MagnetSerializers
    pagination_class = MagnetPagenation
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, OrderingFilter)
    filter_class = MagnetFilter
    search_fields = ('title',)
    ordering_fields = ('create_time','file_size')





