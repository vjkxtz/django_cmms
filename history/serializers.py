from rest_framework import serializers
from .models import Carrier_number, Carrier, Stop_numbers, Stop, Tsw_number, Tsw, Part, Type, Sub_type

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

class Part_serializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class Type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class Sub_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_type
        fields = '__all__'