from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .serializers import AuthorSerializer , GenreSerializer, BookSerializer

from .models import Author, Genre, Book

@api_view(['GET' , 'POST'])
def authors(request:Request):
    if request.method == 'GET':
        categories = Author.objects.all()
        return Response(categories.values() , status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        # save data to database
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            Author.objects.create(**serializer.validated_data)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT','DELETE']) 
def author(request:Request , id:int):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            author.name = serializer.validated_data['name']
            author.bio = serializer.validated_data['bio']
            author.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET' , 'POST'])
def genres(request:Request):
    if request.method == 'GET':
        categories = Genre.objects.all()
        return Response(categories.values() , status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        # save data to database
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            Genre.objects.create(**serializer.validated_data)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

 

@api_view(['GET' , 'PUT','DELETE'])
def genre(request:Request , id:int):
    try:
        obj = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GenreSerializer(obj)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        data = request.data
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            obj.name = serializer.validated_data['name']
            obj.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET' , 'POST'])
def books(request:Request):
    if request.method == 'GET':
        categories = Book.objects.all()
        return Response(categories.values() , status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        try:
            author = Author.objects.get(id=data.get('author_id'))
            genre = Genre.objects.get(id=data.get('genre_id'))
        except (Author.DoesNotExist, Genre.DoesNotExist):
            return Response({'error': 'Author or Genre not found'}, status=status.HTTP_400_BAD_REQUEST)

        # save data to database
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            # Create the book object with author and genre instances
            Book.objects.create(
                title=data['title'],
                author_id=author,  # Pass the actual Author instance
                genre_id=genre,    # Pass the actual Genre instance
                published_date=data['published_date']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

 

@api_view(['GET' , 'PUT','DELETE'])
def book(request:Request , id:int):
    try:
        obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(obj)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            obj.name = serializer.validated_data['name']
            obj.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        
        






