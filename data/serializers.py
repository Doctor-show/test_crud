from rest_framework import serializers
from data.models import Data


class DataDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Data
        fields = '__all__'


class DataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'name', 'description')


