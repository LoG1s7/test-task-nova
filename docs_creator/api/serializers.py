from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериализатор для создания файла"""

    class Meta:
        model = File
        fields = ('id', 'name', 'data')
        read_only_fields = [
            "id",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        return File.objects.create(**validated_data, user_account=user)
