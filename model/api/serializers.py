from rest_framework import serializers

from ..models import Diod


class DiodSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    function = serializers.CharField(required=True)

    class Meta:
        model = Diod
        fields = (
            'id', 'title', 'function', 'down',
        )


class ModelTxtSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    file = serializers.CharField(required=True)

    class Meta:
        model = Diod
        fields = (
            'id', 'title', 'file',
        )
