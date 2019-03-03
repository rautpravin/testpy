from rest_framework import serializers
from .models import *

class CountrySer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

