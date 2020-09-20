from django.test import TestCase
from volunteers.models import Voluntary


class VoluntaryModelTestCase(TestCase):

    def test_create_voluntary(self):
        voluntary = Voluntary.objects.create(
            first_name='Bruce',
            last_name='Wayne',
            neighborhood='Cave',
            city='Gothan',
        )
        self.assertEqual(voluntary.first_name, 'Bruce')
        self.assertEqual(voluntary.last_name, 'Wayne')
        self.assertEqual(voluntary.neighborhood, 'Cave')
        self.assertEqual(voluntary.city, 'Gothan')
        self.assertEqual(str(voluntary), 'Bruce Wayne')
