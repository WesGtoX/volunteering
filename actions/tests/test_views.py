from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .fixture import ActionFactory


class ActionViewSetTests(APITestCase):
    """Action endpoints tests"""

    def setUp(self):
        self.data = {
            'name': 'Fazer o Bem',
            'institution': 'Bem para Todos',
            'address': 'Rua Alameda dos Anjos',
            'neighborhood': 'Cave',
            'city': 'Gotham',
            'description': 'Fazendo o bem sem olhar a quem',
        }

    def test_perform_create(self):
        """Action performe create test"""

        response = self.client.post(reverse('action-list'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertTrue(len(response.data['institution']), self.data['institution'])

    def test_list(self):
        """Action list test"""

        response = self.client.get(reverse('action-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        ActionFactory.create_batch(5)

        response = self.client.get(reverse('action-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 5)

    def test_retrieve(self):
        """Action retrieve test"""

        action = ActionFactory.create(id=10)

        response = self.client.get(reverse('action-detail', args=[11]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(reverse('action-detail', args=[10]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], action.name)
        self.assertEqual(response.data['institution'], action.institution)
        self.assertEqual(response.data['address'], action.address)
        self.assertEqual(response.data['neighborhood'], action.neighborhood)
        self.assertEqual(response.data['city'], action.city)
        self.assertEqual(response.data['description'], action.description)

    def test_update(self):
        """Action update test"""

        action = ActionFactory.create(id=21)
        self.assertNotEqual(action.name, self.data['name'])
        self.assertNotEqual(action.institution, self.data['institution'])

        response = self.client.put(reverse('action-detail', args=[22]), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(reverse('action-detail', args=[21]), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['institution'], self.data['institution'])

    def test_partial_update(self):
        """Action partial update test"""

        action = ActionFactory.create(id=22)
        data = {
            'name': 'Ação para Melhorar',
            'institution': 'Vamos Ajudar',
        }
        self.assertNotEqual(action.name, data['name'])
        self.assertNotEqual(action.institution, data['institution'])

        response = self.client.patch(reverse('action-detail', args=[23]), data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.patch(reverse('action-detail', args=[22]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['institution'], data['institution'])

    def test_destroy(self):
        """Action delete test"""

        ActionFactory.create(id=15)

        response = self.client.get(reverse('action-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)

        response = self.client.delete(reverse('action-detail', args=[16]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('action-detail', args=[15]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('action-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
