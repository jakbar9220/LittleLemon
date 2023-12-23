from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        # Create test instances of the Menu model
        Menu.objects.create(name="Dish 1", price=10.99)
        Menu.objects.create(name="Dish 2", price=8.99)
        Menu.objects.create(name="Dish 3", price=15.50)

    def test_getall(self):
        # Retrieve all Menu objects using the API
        client = APIClient()
        url = reverse('menu')  # Assuming 'menu-list' is the name of your MenuViewSet URL
        response = client.get(url)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the test instances
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
    