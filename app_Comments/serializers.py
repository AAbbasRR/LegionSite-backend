from rest_framework import exceptions, serializers

from .models import Comments


class ListCreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'game',
            'name',
            'opinion',
            'rate',
        ]

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)
