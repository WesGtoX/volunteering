from django.test import TestCase
from actions.models import Action


class ActionModelTestCase(TestCase):

    def test_create_action(self):
        action = Action.objects.create(
            name='Fazer o Bem',
            institution='Bem para Todos',
            address='Rua Alameda dos Anjos',
            neighborhood='Cave',
            city='Gotham',
            description='Fazendo o bem sem olhar a quem',
        )
        self.assertEqual(action.name, 'Fazer o Bem')
        self.assertEqual(action.institution, 'Bem para Todos')
        self.assertEqual(action.address, 'Rua Alameda dos Anjos')
        self.assertEqual(action.neighborhood, 'Cave')
        self.assertEqual(action.city, 'Gotham')
        self.assertEqual(action.description, 'Fazendo o bem sem olhar a quem')
        self.assertEqual(str(action), 'Fazer o Bem')
