from .models import Restaurants
from rest_framework import serializers


class RestaurantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('id', 'slug', 'title', 'description', 'body', 'owner_id')