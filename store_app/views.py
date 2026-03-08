from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from store_app.forms import ProductForm, CategoryForm
from store_app.models import Product, Category


# Create your views here.
def index(request):
    return render(request, "store_app/main_page.html")


def about(request):
    return render(request, "store_app/about_page.html")


def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(
        request,
        "store_app/products_list.html",
        context=context,
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product,
    }
    return render(
        request,
        "store_app/product_detail.html",
        context=context,
    )


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products_list")
    else:
        form = ProductForm()
    context = {
        "title": "Добавление нового товара",
        "button_name": "Добавить товар",
        "form": form,
    }
    return render(
        request,
        "store_app/add_or_edit_prod_or_cat.html",
        context=context,
    )


def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products_list")
    else:
        form = ProductForm(instance=product)
    context = {
        "title": "Изменение карточки товара",
        "button_name": "Сохранить изменения",
        "form": form,
    }
    return render(
        request,
        "store_app/add_or_edit_prod_or_cat.html",
        context=context,
    )


def categories_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(
        request,
        "store_app/categories_list.html",
        context=context,
    )


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = CategoryForm()
    context = {
        "title": "Добавление новой категории",
        "button_name": "Добавить категорию",
        "form": form,
    }
    return render(
        request,
        "store_app/add_or_edit_prod_or_cat.html",
        context=context,
    )


def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(
            request.POST, instance=category
        )
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = CategoryForm(instance=category)
    context = {
        "title": "Изменение категории",
        "button_name": "Сохранить изменения",
        "form": form,
    }
    return render(
        request,
        "store_app/add_or_edit_prod_or_cat.html",
        context=context,
    )
