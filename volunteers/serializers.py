from rest_framework import serializers
from .models import Voluntary


class VoluntarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Voluntary
        fields = [
            'id',
            'first_name',
            'last_name',
            'neighborhood',
            'city',
        ]
