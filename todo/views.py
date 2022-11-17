from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Category, Task
)
from .serializers import (
    CategorySerializer, TodoSerializer
)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_list(request):
    tasks = Task.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)
