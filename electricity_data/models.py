from django.db import models

# Create your models here.
class ElectricityData(models.Model):
    intervalstarttime_gmt = models.DateTimeField()
    intervalendtime_gmt = models.DateTimeField()
    opr_dt = models.DateField()
    opr_hr = models.IntegerField()
    node_id_xml = models.CharField(max_length=128)
    node_id = models.CharField(max_length=128)
    node = models.CharField(max_length=128)
    market_run_id = models.CharField(max_length=128)
    lmp_type = models.CharField(max_length=64)
    xml_data_item = models.CharField(max_length=128)
    pnode_resmrid = models.CharField(max_length=128)
    grp_type = models.CharField(max_length=128)
    pos = models.IntegerField()
    prc = models.FloatField()
    opr_interval = models.IntegerField()
    group = models.IntegerField()
