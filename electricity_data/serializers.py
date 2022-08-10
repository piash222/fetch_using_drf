from rest_framework import serializers
from .models import ElectricityData


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityData
        fields = ['id', 'intervalstarttime_gmt', 'intervalendtime_gmt', 'opr_dt', 'opr_hr', 'node_id_xml', 'node_id',
                  'node', 'market_run_id', 'lmp_type', 'xml_data_item', 'pnode_resmrid', 'grp_type', 'pos', 'prc',
                  'opr_interval', 'group']
