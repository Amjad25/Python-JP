from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    bio = serializers.CharField(required=True, max_length=500)
    
class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField(required=True, max_length=50)
    

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    author_id = serializers.IntegerField(required=True)
    genre_id = serializers.IntegerField(required=True)
    published_date = serializers.DateField(required=True)


