from dataclasses import field
from rest_framework import serializers
from .models import Quiz

class QuizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')

