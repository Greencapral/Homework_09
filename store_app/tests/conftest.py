import pytest
from store_app.models import Product, Category



@pytest.fixture
def category_1():
    """
    Фикстура pytest для создания тестовой категории.
    Создаёт и возвращает экземпляр модели Category с предустановленным именем.
    Используется в тестах как зависимый объект для других фикстур или тестов.
    Returns:
        Category: экземпляр модели Category с именем «Тестовая категория»
    """
    return Category.objects.create(name="Тестовая категория")



@pytest.fixture
def product_1(category_1):
    """
    Фикстура pytest для создания тестового продукта.
    Создаёт и возвращает экземпляр модели Product с предустановленными полями.
    Зависит от фикстуры category_1 — использует созданную ей категорию.
    Args:
        category_1 (Category): фикстура, предоставляющая тестовую категорию.
            Передаётся автоматически благодаря механизму зависимостей фикстур pytest.
    Returns:
        Product: экземпляр модели Product
    """
    return Product.objects.create(
        name="тестовый продукт №1",
        price=33.33,
        category=category_1,
    )
