from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    # email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    onwer = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    # related_product = ProductInlineSerializer(
    #     source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)

    # email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                              validators.unique_products_title])

    class Meta:
        model = Product
        fields = [
            'onwer',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            # 'my_discount',
            # 'my_user_data',
            # 'email',
            # 'related_product'
        ]

    def get_my_user_data(self, obj):
        return {
            'username': obj.user.username,
        }

    # validators.py
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already Product name!. try another one ")
    #     return value

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super(ProductSerializer, self).create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     # return super().update(instance, validated_data)
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('products-edit', kwargs={'pk': obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()
