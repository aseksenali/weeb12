from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Product, Category


def all_products(req):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def all_categories(req):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def get_product(req, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())


def get_category(req, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json())


def get_products_by_category(req, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)
