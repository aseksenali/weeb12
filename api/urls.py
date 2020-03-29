from django.urls import path

from api.views import *

urlpatterns = [
    path('products/', all_products),
    path('products/<int:product_id>', get_product),
    path('categories/', all_categories),
    path('categories/<int:category_id>', get_category),
    path('categories/<int:category_id>/products', get_products_by_category)
]
