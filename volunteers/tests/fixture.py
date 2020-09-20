import factory
from volunteers.models import Voluntary


class VoluntaryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Voluntary

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    neighborhood = factory.Faker('street_name')
    city = factory.Faker('city')
