from .models import Points, Adm
from rest_framework import serializers


class PointsSerializer(serializers.Serializer):

    dcount = serializers.IntegerField()
    type = serializers.CharField(max_length=80)

    class Meta:
        model = Points
        fields = '__all__'


class AdmSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=254)
    geom = serializers.CharField(max_length=2000)

    class Meta:
        model = Adm
        fields = ('name', 'area')