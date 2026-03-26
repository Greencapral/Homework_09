from django.contrib import admin
from django.urls import path

from .views import (
    index,
    about,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    categories_list,
    category_add,
    category_edit,
)

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path(
        "products_list/",
        ProductListView.as_view(),
        name="products_list",
    ),
    path(
        "products_list/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "products_list/<int:pk>/edit/",
        ProductUpdateView.as_view(),
        name="product_edit",
    ),
    path(
        "products_list/add/",
        ProductCreateView.as_view(),
        name="product_add",
    ),
    path(
        "products_list/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
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
