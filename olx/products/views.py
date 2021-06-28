from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from products.models import Product
from django.db.models import Q
# Create your views here.

class productList(ListView):

    model = Product
    template_name = "product_list.html"


class productDetails(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "prod"


class searchView(ListView):
    model = Product
    template_name = "search_list.html"
    context_object_name = "searchedres"
    def get_queryset(self):
        query = self.request.GET['search']
        return Product.objects.filter(sold=False).filter(Q(name__contains=query)|Q(company__contains=query))
