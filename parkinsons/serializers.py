from rest_framework import serializers

class UploadFileFormSerializer(serializers.Serializer):
    class Meta:
        title = serializers.CharField()
        file = serializers.FileField()