from django.shortcuts import render

# Create your views here.
from electricity_data.models import ElectricityData
from electricity_data.serializers import DataSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class DataList(generics.ListAPIView):
    queryset = ElectricityData.objects.all()
    serializer_class = DataSerializer
    pagination_class = PageNumberPagination
    search_fields = ('node_id_xml', 'node_id', 'node', 'market_run_id','lmp_type', 'xml_data_item', 'pnode_resmrid','grp_type')


class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElectricityData.objects.all()
    serializer_class = DataSerializer