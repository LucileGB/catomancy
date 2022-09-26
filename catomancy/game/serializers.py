from rest_framework import serializers

from .models import Cat, Player

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ['url', 'name', 'owner', 'affection', 'time_created']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'player', 'house', 'money']