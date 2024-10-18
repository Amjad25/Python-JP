from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .models import Product, Category, Supplier
from .serializers import CategorySerializer, ProductSerializer, SupplierSerializer

@api_view(['GET', 'POST'])
def products(request: Request):
    if request.method == 'GET':
        # Fetch all products and return them
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        # Deserialize the incoming product data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            try:
                # Fetch Category instance if provided
                category = None
                if data.get('category_id'):
                    category = Category.objects.get(id=data.get('category_id'))
                
                # Fetch Supplier instances
                suppliers = Supplier.objects.filter(id__in=data.get('suppliers'))
                # if suppiler not found
                suppliers_count = suppliers.count()
                
                if suppliers_count != len(data.get('suppliers')):
                    return Response({"error": "One or more suppliers not found."}, status=status.HTTP_400_BAD_REQUEST)

                # Create the Product instance
                product = Product.objects.create(
                    name=data.get('name'),
                    description=data.get('description'),
                    price=data.get('price'),
                    quantity=data.get('quantity'),
                    category=category
                )

                # Assign suppliers to the product
                product.suppliers.set(suppliers)
                product.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Category.DoesNotExist:
                return Response({"error": "Category not found."}, status=status.HTTP_400_BAD_REQUEST)

            except Supplier.DoesNotExist:
                return Response({"error": "One or more suppliers not found."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product(request : Request,id:int):
    product_id = id
    if request.method == 'GET':   
        try:
            product = Product.objects.get(id=product_id)
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'PUT':
        try:
            product = Product.objects.get(id=product_id)
            data = request.data
            serializer = ProductSerializer(product, data=data)
            if serializer.is_valid():
                # Fetch Category instance if provided
                category = None
                if data.get('category_id'):
                    category = Category.objects.get(id=data.get('category_id'))
                
                # Fetch Supplier instances
                suppliers = Supplier.objects.filter(id__in=data.get('suppliers'))
                # if suppiler not found
                suppliers_count = suppliers.count()
                
                if suppliers_count != len(data.get('suppliers')):
                    return Response({"error": "One or more suppliers not found."}, status=status.HTTP_400_BAD_REQUEST)

                # Update the Product instance
                product.name = data.get('name')
                product.description = data.get('description')
                product.price = data.get('price')
                product.quantity = data.get('quantity')
                product.category = category

                # Assign suppliers to the product
                product.suppliers.set(suppliers)
                product.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)        
        
        
@api_view(['GET', 'POST'])
def categories(request: Request):
    if request.method == 'GET':
        # Fetch all categories
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            Category.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def category(request:Request,id:int):
    category_id =id
    try:
        category = Category.objects.get(category_id)
    except Category.DoesNotExist:
        Response({'error':'Category Not Found'},status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        data = request.data
        category_serializer = CategorySerializer(category,data=data)
        
        if category_serializer.is_valid():
            category.name = data.get('name')
            category.description = data.get('description')
            category.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            category.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_200_OK) 

@api_view(['GET', 'POST'])
def suppliers(request: Request):
    if request.method == 'GET':
        # Fetch all suppliers
        suppliers = Supplier.objects.all()
        supplier_serializer = SupplierSerializer(suppliers, many=True)
        return Response(supplier_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = SupplierSerializer(data=data)

        if serializer.is_valid():
            Supplier.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def supplier(request:Request,id:int):
    supplier_id =id
    try:
        supplier = Supplier.objects.get(supplier_id)
    except Supplier.DoesNotExist:
        Response({'error':'Supplier Not Found'},status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        supplier_serializer = SupplierSerializer(supplier)
        return Response(supplier_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        data = request.data
        supplier_serializer = SupplierSerializer(supplier,data=data)
        
        if supplier_serializer.is_valid():
            supplier.name = data.get('name')
            supplier.description = data.get('description')
            supplier.save()
            return Response(supplier_serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            supplier.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_200_OK) 


