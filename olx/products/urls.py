from django.urls import path
from products.views import productList,productDetails,searchView

app_name = "products"

urlpatterns=[
    path("", productList.as_view(), name = "productlist"),
    path("item/<int:pk>", productDetails.as_view(), name = "details"),
    path("search/", searchView.as_view(), name="search"),
]
