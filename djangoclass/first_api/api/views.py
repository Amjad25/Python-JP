from rest_framework.response import Response
from rest_framework import status 
from rest_framework.request import Request
from rest_framework.decorators import api_view

@api_view(['GET' , 'POST'])
def get_post_users(request:Request):
    if request.method == 'GET':
        
        person = [{"name": "danish", "email": "danish@gmail.com"}]
        return Response(person , status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        return Response(data , status=status.HTTP_201_CREATED)
    
    return Response({"message": "Hello, world!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'PUT' , 'DELETE', 'PATCH'])
def get_put_delete_patch_user(request:Request , pk):
    if request.method == 'GET':
        q_params = request.query_params
        print(q_params)
        person = {"name": "danish", "email": "danish@gmail.com"}
        return Response(person , status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = "update user put"
        return Response(data , status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        data = "delete user"
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PATCH':
        data = "update user patch"
        return Response(data , status=status.HTTP_201_CREATED)
    
    return Response({"message": "Hello, world!"}, status=status.HTTP_400_BAD_REQUEST)





