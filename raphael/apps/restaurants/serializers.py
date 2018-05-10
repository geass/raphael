from .models import Restaurants
from rest_framework import serializers
from rest_framework.exceptions import APIException
from slugify import slugify

class RestaurantsSerializer(serializers.HyperlinkedModelSerializer):

	def update(self, instance, validated_data):

		if validated_data['owner_id'] != instance.owner_id:

			raise APIException("Unauthorized Access!")

		instance.slug = slugify(validated_data['title'])
		instance.title = validated_data['title']
		instance.description = "12312123"
		instance.body = validated_data['body']
		instance.save()

		return instance

	class Meta:
		model = Restaurants
		fields = ('id', 'slug', 'title', 'description', 'body', 'owner_id')