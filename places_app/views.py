from django.shortcuts import render
from .models import Place
from rest_framework import generics
from .serializers import PlaceSerializer
from django.contrib.postgres.search import SearchVector
# Create your views here.


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDeleteView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceSearchView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query')
        if query:
            return Place.objects.annotate(search = SearchVector('name', 'description')).filter(search=query)
        return Place.objects.none()
