from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list),
    path('categories/', views.category_list),

]