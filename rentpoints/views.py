# -*- coding: utf-8 -*-
from django.db.models import Count
from .models import Points, Adm
from django.http import JsonResponse
import collections


def points_in_adm(request, id):

    adm = Adm.objects.get(gid=id)
    points_in_adm = collections.Counter()
    for p in Points.objects.all():
        if adm.geom.intersects(p.geom):
            points_in_adm[p.type] += 1

    points_type_all = Points.objects.values('type').annotate(dcount=Count('type'))
    points_types_adm = []
    for st in points_type_all:
        points_types_adm.append(dict(type=st["type"],
                                 count_points=points_in_adm[st["type"]],
                                 procent_points=points_in_adm[st["type"]]*100/st["dcount"]))
    return JsonResponse(points_types_adm, safe=False)

