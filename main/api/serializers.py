from rest_framework import serializers

class ResultSerachSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=30)
    keywords = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=120)
    link = serializers.EmailField()
    positionID = serializers.IntegerField()
    