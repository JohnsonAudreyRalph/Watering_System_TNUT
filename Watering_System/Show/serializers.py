from rest_framework import serializers
from .models import API_HaoDat, API_KheCoc, API_ThaiMinh


class Data_Serializer_HaoDat(serializers.ModelSerializer):
    class Meta:
        model = API_HaoDat
        fields = '__all__'

class Data_Serializer_KheCoc(serializers.ModelSerializer):
    class Meta:
        model = API_KheCoc
        fields = '__all__'

class Data_Serializer_ThaiMinh(serializers.ModelSerializer):
    class Meta:
        model = API_ThaiMinh
        fields = '__all__'