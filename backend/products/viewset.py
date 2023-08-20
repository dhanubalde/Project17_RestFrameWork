from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> a list of products -> queryset
    get -> retrieve a list of products -> Product instance Details View
    post -> create a new product -> instance 
    put -> update a product -> instance
    patch -> partially update a product -> instance
    delete -> remove a product -> instance
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    '''
    get ->  list -> queryset
    get -> retrieve -> Product instance Details View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
# product_detail_view = ProductGenericViewSet.as_view({'get': 'retreive'})
