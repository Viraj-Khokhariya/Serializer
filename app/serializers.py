from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.Serializer):
    #id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)