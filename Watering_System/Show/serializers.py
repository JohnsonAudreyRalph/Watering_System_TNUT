from rest_framework import serializers
from .models import API_HaoDat_R_W, API_HaoDat_read, API_KheCoc_R_W, API_KheCoc_read, API_ThaiMinh_R_W, API_ThaiMinh_read


class Data_Serializer_HaoDat_R_W(serializers.ModelSerializer):
    class Meta:
        model = API_HaoDat_R_W
        fields = '__all__'

class Data_Serializer_KheCoc_R_W(serializers.ModelSerializer):
    class Meta:
        model = API_KheCoc_R_W
        fields = '__all__'

class Data_Serializer_ThaiMinh_R_W(serializers.ModelSerializer):
    class Meta:
        model = API_ThaiMinh_R_W
        fields = '__all__'

class Data_Serializer_HaoDat_read(serializers.ModelSerializer):
    class Meta:
        model = API_HaoDat_read
        fields = '__all__'

class Data_Serializer_KheCoc_read(serializers.ModelSerializer):
    class Meta:
        model = API_KheCoc_read
        fields = '__all__'

class Data_Serializer_ThaiMinh_read(serializers.ModelSerializer):
    class Meta:
        model = API_ThaiMinh_read
        fields = '__all__'