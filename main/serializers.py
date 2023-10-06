from rest_framework import serializers

from .models import Data


class DataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ("id", "fullName", "shortName", "address")


class DataDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'
