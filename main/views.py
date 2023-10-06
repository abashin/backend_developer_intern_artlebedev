from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework as rest_filters, CharFilter, NumberFilter

from django_filters.rest_framework import DjangoFilterBackend
from .models import Data
from .serializers import DataListSerializer, DataDetailSerializer



class DataFilter(rest_filters.FilterSet):

    fullName = CharFilter(field_name="fullName", lookup_expr='icontains')

    class Meta:
        model = Data
        fields = ['fullName']

class DataListView(generics.ListAPIView):
    serializer_class = DataListSerializer
    queryset = Data.objects.all()
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = DataFilter
    search_fields = ['fullName']


class DataDetailView(APIView):
    def get(self, request, pk):
        data = Data.objects.get(id=pk)
        serializer = DataDetailSerializer(data)
        return Response(serializer.data)