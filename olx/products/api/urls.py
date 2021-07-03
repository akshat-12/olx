from django.urls import path
from products.api.views import product_list_view

urlpatterns = [
    path("products/", product_list_view, name="product-list")
]