
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Place

class PlaceAPITests(TestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'description': 'This is a test place',
            'latitude': 1.234567,
            'longitude': 2.345678,
        }
        self.place = Place.objects.create(**self.place_data)

    def test_create_place(self):
        url = reverse('place-list-create')
        response = self.client.post(url, self.place_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_places_list(self):
        url = reverse('place-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_places(self):
        url = reverse('place-search')
        response = self.client.get(url, {'query': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

