from rest_framework import serializers
from .models import *

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['categories']