from dataclasses import field
from wsgiref.validate import validator
from rest_framework import serializers

from .models import *

class PaletteSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        print('hi', len(data['dominant_color']))
        if len(data['dominant_color'])<1 or len(data['dominant_color'])>2:
            raise serializers.ValidationError("dominant_color error")
        elif len(data['accent_color'])<2 or len(data['accent_color'])>5:
            raise serializers.ValidationError("accent_color error")
        else:
            return data
    class Meta:
        model = Palette
        fields = '__all__'

class FavoritePaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoritePalette
        fields = '__all__'
