from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.relations import method_overridden
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from products.models import Product
from products.api.serializers import ProductSerializer

@api_view(["GET", "POST"])
def product_list_view(request):
    if request.method == "GET":
        products = Product.objects.filter(sold=False)
        serializer_context = {
            'request': request,
        }

        serializer = ProductSerializer(products, many=True, context=serializer_context)
        return Response(serializer.data)
    elif request.method == "POST":
        # To Do: Add serializer for image
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
