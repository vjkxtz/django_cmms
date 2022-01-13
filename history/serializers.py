from rest_framework import serializers
from .models import Carrier_number, Carrier, Stop_numbers, Stop, Tsw_number, Tsw

class Carrier_number_serializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier_number
        fields = '__all__'


class Carrier_serializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = '__all__'

class Stop_number_serializer(serializers.ModelSerializer):
    class Meta:
        model = Stop_numbers
        fields = '__all__'

class Stop_serializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'

class Tsw_number_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tsw_number
        fields = '__all__'

class Tsw_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tsw
        fields = '__all__'