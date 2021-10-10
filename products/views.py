from django.http import JsonResponse
from .models import Manufacturer, Products

# from django.views.generic import DetailView, ListView
# class ProductListView(ListView):
#     model = Products
#     template_name = "products/product_list.html"
#
# class ProductDetailView(DetailView):
#     model = Products
#     template_name = "products/product_detail.html"

def product_list(request):
    products = Products.objects.all()
    data = {
        "products": list(products.values())
    }
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Products.objects.get(pk=pk)
        data = {
            "product": {
                "name":product.name,
                "manufacturer": product.manufacturer.name,
                "quantity": product.quantity,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "description": product.description,
                "photo": product.photo.url
            }
        }
        responce = JsonResponse(data)
    except Products.DoesNotExist:
        responce = JsonResponse(
            {
                "error": {
                    "code": 404,
                    "message": "product not found"
                }
            }, status=404
        )
    return responce

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(is_active=True)
    data = {
        "manufacturers": list(manufacturers.values())
    }
    response = JsonResponse(data)
    return response

def manufacturer_details(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "is_active": manufacturer.is_active,
                "products": list(manufacturer_products.values())
            }
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Not a registered manufucturer!"
            }
        }, status=404)
    return response