from django.urls import path
from .views import product_list, product_detail, manufacturer_list, manufacturer_details# ProductListView, ProductDetailView

urlpatterns = [
    # path('', ProductListView.as_view(), name='product-list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail')
    path('product-list/', product_list, name='product-list'),
    path('product-detail/<int:pk>/', product_detail, name='product-detail'),
    path('manufacturer-list/', manufacturer_list, name='manufacturer-list'),
    path('manufacturer-detail/<int:pk>/', manufacturer_details, name='manufacturer-detail')
]