from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = [
            'id',
            'name',
            'institution',
            'address',
            'neighborhood',
            'city',
            'description',
        ]
