from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from . import views

# api/products/
urlpatterns = [
    # path('', views.product_mixin_view),
    # path('auth', obtain_auth_token),
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    # path('<int:pk>/', views.product_mixin_view),
    path('<int:pk>/update/', views.product_update_view, name='products-edit'),
    path('<int:pk>/delete/', views.product_destroy_view),
]
