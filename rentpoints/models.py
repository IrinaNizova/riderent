#from django.db import models
from django.contrib.gis.db import models


class Points(models.Model):
    gid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=80)
    num = models.BigIntegerField()
    geom = models.PointField()

    def __str__(self):
        return "-".join((self.type, str(self.num)))

    class Meta:
        db_table = 'points'


class Adm(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    okato_code = models.CharField(max_length=11)
    area = models.IntegerField()
    geom = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'adm'