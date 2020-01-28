from rest_framework import serializers
from .models import *
# from rest_framework import Book

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'