


from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view

@api_view(('GET',))
def product_get(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
