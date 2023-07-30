from django.urls import path
from .views import PlaceListCreateView, PlaceDeleteView, PlaceSearchView


urlpatterns = [
    path('api/places/', PlaceListCreateView.as_view(), name='place-list-create'),
    path('api/places/<int:pk>/', PlaceDeleteView.as_view(), name='place-delete'),
    path('api/places/search/', PlaceSearchView.as_view(), name='place-search')

]