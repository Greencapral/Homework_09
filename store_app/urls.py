from django.contrib import admin
from django.urls import path

from .views import (
    index,
    about,
    products_list,
    product_detail,
    product_add,
    product_edit,
    categories_list,
    category_add,
    category_edit,
)

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path(
        "products_list/",
        products_list,
        name="products_list",
    ),
    path(
        "products_list/<int:product_id>/",
        product_detail,
        name="product_detail",
    ),
    path(
        "products_list/<int:product_id>/edit/",
        product_edit,
        name="product_edit",
    ),
    path(
        "products_list/add/",
        product_add,
        name="product_add",
    ),
    path(
        "categories_list/",
        categories_list,
        name="categories_list",
    ),
    path(
        "categories_list/<int:category_id>/edit/",
        category_edit,
        name="category_edit",
    ),
    path(
        "categories_list/add/",
        category_add,
        name="category_add",
    ),
]
