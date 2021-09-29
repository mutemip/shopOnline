from django.views.generic import DetailView, ListView
from .models import Manufacturer, Products

class ProductListView(ListView):
    model = Products
    template_name = "products/product_list.html"

class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"
