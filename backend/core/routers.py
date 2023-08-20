from rest_framework.routers import DefaultRouter

from products.viewset import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')
# print(router.urls)
urlpatterns = router.urls
