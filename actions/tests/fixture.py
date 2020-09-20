import factory
from actions.models import Action


class ActionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Action

    name = factory.Faker('company_suffix')
    institution = factory.Faker('company')
    address = factory.Faker('street_address')
    neighborhood = factory.Faker('street_name')
    city = factory.Faker('city')
    description = factory.Faker('sentence')
