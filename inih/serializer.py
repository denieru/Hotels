from rest_framework import serializers
from .models import inih


class inihSerializer(serializers.ModelSerializer):
    class Meta:
        model = inih
        fields = '__all__' 