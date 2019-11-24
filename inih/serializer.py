from rest_framework import serializers
from .models import inih, menu, servh,archivo,habh


class inihSerializer(serializers.ModelSerializer):
    class Meta:
        model = inih
        fields = '__all__' 

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class servhSerializer(serializers.ModelSerializer):
    class Meta:
        model = servh
        fields = '__all__'

class archSerializer(serializers.ModelSerializer):
    class Meta:
        model = archivo
        fields = "__all__"
class habhSerializer(serializers.ModelSerializer):
    class Meta:
        model = habh
        fields = "__all__"
