from .serializers import HeroSerializer
from rest_framework import viewsets
from .models import Hero
from django.http import  JsonResponse


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


def heroes_list(request):
    queryset = Hero.objects.all().order_by('name')
    serializer = HeroSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_hero(request, hero_id):
    query = Hero.objects.get(id=hero_id)
    serializer = HeroSerializer(query)
    return JsonResponse(serializer.data, safe=False)


