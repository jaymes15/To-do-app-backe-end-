from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from contentapi.models import Item
from contentapi.serializers import ItemSerializer


# Create your views here.


class ItemVeiwSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


