from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from store_app.forms import ProductForm, CategoryForm
from store_app.models import Product, Category


def index(request):
    """
    Отображает главную страницу интернет‑магазина.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон главной страницы.
    """
    return render(request, "store_app/main_page.html")


def about(request):
    """
    Отображает страницу «О нас» с информацией о магазине.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон страницы «О нас».
    """
    return render(request, "store_app/about_page.html")


def products_list(request):
    """
    Отображает список всех товаров в магазине.

    Получает все объекты Product из базы данных и передаёт их в шаблон
    для отображения в виде списка.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон со списком товаров.
    """
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
    """
    Отображает подробную информацию о конкретном товаре.

    Ищет товар по ID. Если товар не найден, возвращает ошибку 404.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.
        product_id (int): ID товара в базе данных.

    Returns:
        HttpResponse: Отрендеренный шаблон с деталями товара.
    """
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
    """
    Обрабатывает добавление нового товара через форму.

    Если метод запроса — POST и форма валидна, сохраняет новый товар
    и перенаправляет на страницу списка товаров. В противном случае отображает
    пустую форму для заполнения.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон формы добавления товара или
        перенаправление на список товаров.
    """
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
    """
    Обрабатывает редактирование существующего товара.

    Получает товар по ID, отображает форму с его данными. При отправке POST‑запроса
    с валидными данными сохраняет изменения и перенаправляет на список товаров.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.
        product_id (int): ID редактируемого товара.

    Returns:
        HttpResponse: Отрендеренный шаблон формы редактирования товара или
        перенаправление на список товаров.
    """
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
    """
    Отображает список всех категорий товаров.

    Получает все объекты Category из базы данных и передаёт их в шаблон
    для отображения в виде списка.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон со списком категорий.
    """
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
    """
    Обрабатывает добавление новой категории через форму.

    Если метод запроса — POST и форма валидна, сохраняет новую категорию
    и перенаправляет на страницу списка категорий. В противном случае отображает
    пустую форму для заполнения.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.

    Returns:
        HttpResponse: Отрендеренный шаблон формы добавления категории или
        перенаправление на список категорий.
    """
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
    """
    Обрабатывает редактирование существующей категории.

    Получает категорию по ID, отображает форму с её данными. При отправке
    POST‑запроса с валидными данными сохраняет изменения и перенаправляет
    на список категорий.

    Args:
        request (HttpRequest): HTTP‑запрос от клиента.
        category_id (int): ID редактируемой категории.

    Returns:
        HttpResponse: Отрендеренный шаблон формы редактирования категории или
        перенаправление на список категорий.
    """
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
