from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .fixture import VoluntaryFactory


class VoluntaryViewSetTests(APITestCase):
    """Voluntary endpoints tests"""

    def setUp(self):
        self.data = {
            'first_name': 'Brune',
            'last_name': 'Wayne',
            'neighborhood': 'Cave',
            'city': 'Gotham',
        }

    def test_perform_create(self):
        """Voluntary performe create test"""

        response = self.client.post(reverse('voluntary-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], self.data['first_name'])
        self.assertTrue(len(response.data['last_name']), self.data['last_name'])

    def test_list(self):
        """Voluntary list test"""

        response = self.client.get(reverse('voluntary-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        VoluntaryFactory.create_batch(5)

        response = self.client.get(reverse('voluntary-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        """Voluntary retrieve test"""

        voluntary = VoluntaryFactory.create(id=10)

        response = self.client.get(reverse('voluntary-detail', args=[11]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('voluntary-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], voluntary.first_name)
        self.assertEqual(response.data['last_name'], voluntary.last_name)
        self.assertEqual(response.data['neighborhood'], voluntary.neighborhood)
        self.assertEqual(response.data['city'], voluntary.city)

    def test_update(self):
        """Voluntary update test"""

        voluntary = VoluntaryFactory.create(id=21)
        self.assertNotEqual(voluntary.first_name, self.data['first_name'])
        self.assertNotEqual(voluntary.last_name, self.data['last_name'])

        response = self.client.put(reverse('voluntary-detail', args=[22]), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('voluntary-detail', args=[21]), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.data['first_name'])
        self.assertEqual(response.data['last_name'], self.data['last_name'])

    def test_partial_update(self):
        """Voluntary partial update test"""

        voluntary = VoluntaryFactory.create(id=22)
        data = {
            'first_name': 'Jane',
            'last_name': 'Joe',
        }
        self.assertNotEqual(voluntary.first_name, data['first_name'])
        self.assertNotEqual(voluntary.last_name, data['last_name'])

        response = self.client.patch(reverse('voluntary-detail', args=[23]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.patch(reverse('voluntary-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    def test_destroy(self):
        """Voluntary delete test"""

        VoluntaryFactory.create(id=15)

        response = self.client.get(reverse('voluntary-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.client.delete(reverse('voluntary-detail', args=[16]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('voluntary-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('voluntary-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
