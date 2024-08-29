from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'author', 'created_at']
        extra_kwargs = {'author': {'read_only': True}}
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        note = Note.objects.create(**validated_data)
        return note
