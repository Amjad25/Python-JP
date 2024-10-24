from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,ListCreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serilizers import *
# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #  /app/category/recent
    @action(detail=False, methods=['get'])
    def recent(self,request):
        category_model =self.get_queryset()
        category_serializer = self.get_serializer(category_model ,many=True)
        return Response(category_serializer.data)

    #  /app/category/1/recent
    @action(detail=False, methods=['get'])
    def recent(self,request,pk=None):
        category =self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data)


class SupplierviewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class =SupplierSerilizer



class ProductviewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =ProductSerilizer





class SupplierListCreateAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class =SupplierSerilizer


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView,):
    queryset =Supplier.objects.all()
    serializer_class = SupplierSerilizer
    



