from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'created_at', 'due_date', 'completed']
        extra_kwargs = {'user': {'read_only': True}}