from django.db.models import Count
from .models import Points, Adm
from django.http import JsonResponse
from .serializer import PointsSerializer, AdmSerializer
from rest_framework import generics


def points_statistic(request):
    queryset = Points.objects.values('type').annotate(dcount=Count('type'))
    serializer = PointsSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


class AdmDetail(generics.RetrieveAPIView):
    queryset = Adm.objects.all()
    serializer_class = AdmSerializer
    lookup_field = 'gid'

