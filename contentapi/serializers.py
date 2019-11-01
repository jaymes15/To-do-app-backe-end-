from rest_framework import serializers
from contentapi.models import Item

class ItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ( 'id', 'title', 'description')
