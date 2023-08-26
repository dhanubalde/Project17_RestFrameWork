from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

from api.mixins import (StaffEditorPermissionMixin, UserQuerySetMixin)
# from api.auth import TokenAuthentication
# from ..api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer
# from django.shortcuts import get_list_or_404
from django.http import Http404


class ProductListCreateAPIView(
        UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # allow_staff_view = False

    # api/auth.py
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    # ]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # api/mixin.py
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()

# details_view url path


class ProductDetailAPIView(
        UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()

# update view url path


class ProductUpdateAPIView(
        UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()



# delete view url path


class ProductDeleteAPIView(
        UserQuerySetMixin,
        StaffEditorPermissionMixin,
        generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDeleteAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
# product_list_view = ProductListAPIView.as_view()


# class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
#     pass


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view con"
        serializer.save()


product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  # put -> update or destroy -> delete

    if method == "GET":
        if pk is not None:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                raise Http404
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True). data
        return Response(data)
    if method == "POST":
        # create an Item object
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
