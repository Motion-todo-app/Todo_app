from rest_framework import serializers
from todo.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'