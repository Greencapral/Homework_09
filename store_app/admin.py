from django.contrib import admin
from store_app.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Product.

    Отображает список товаров с основными полями, предоставляет фильтрацию,
    поиск, сортировку и действие для увеличения цены на 10 %.
    """

    list_display = (
        "name",
        "price",
        "category",
        "created_at",
        "updated_at",
    )
    # Поля, отображаемые в списке товаров в админ‑панели.

    list_filter = ("category",)
    # Поля для фильтрации списка товаров.

    search_fields = ("name",)
    # Поля, по которым доступен поиск товаров.

    search_help_text = (
        "Введите наименование товара для поиска"
    )
    # Текст подсказки для поля поиска.

    ordering = ("-created_at",)
    # Сортировка списка товаров по дате создания (новые сверху).

    date_hierarchy = "created_at"
    # Иерархия дат по полю created_at для удобной навигации.

    readonly_fields = ("created_at", "updated_at")
    # Поля, доступные только для чтения (не редактируются в форме).

    fields = (
        "name",
        "price",
        "category",
    )
    # Поля, отображаемые при редактировании/создании товара.

    @admin.action(description="Изменить цену на +10 %")
    def price_increment(self, request, queryset):
        """
        Действие для массового изменения цены товаров на +10 %.

        Args:
            request: HTTP‑запрос от пользователя.
            queryset: Набор объектов Product, выбранных для обработки.
        """
        for product in queryset:
            product.price = round(product.price * 1.10, 2)
            product.save()

    actions = [
        price_increment,
    ]
    # Список доступных действий для выбранных объектов в админ‑панели.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Category.

    Отображает список категорий с основными полями, предоставляет поиск,
    сортировку и защиту полей created_at и updated_at от редактирования.
    """

    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    # Поля, отображаемые в списке категорий в админ‑панели.

    search_fields = ("name",)
    # Поля, по которым доступен поиск категорий.

    search_help_text = (
        "Введите наименование категории товара для поиска"
    )
    # Текст подсказки для поля поиска.

    ordering = ("-created_at",)
    # Сортировка списка категорий по дате создания (новые сверху).

    date_hierarchy = "created_at"
    # Иерархия дат по полю created_at для удобной навигации.

    readonly_fields = ("created_at", "updated_at")
    # Поля, доступные только для чтения (не редактируются в форме).

    fields = ("name",)
    # Поле, отображаемое при редактировании/создании категории.
