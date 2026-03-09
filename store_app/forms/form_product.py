from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from store_app.models import Product


class ProductForm(ModelForm):
    """
    Форма для создания и редактирования товаров.

    Наследует ModelForm для автоматической генерации полей на основе модели Product.
    Содержит кастомную валидацию поля name — проверяет, что длина названия
    не менее 5 символов. Использует кастомные виджеты с CSS‑классами для улучшения
    визуального отображения в интерфейсе.
    """

    class Meta:
        """
        Метаданные формы, определяющие связь с моделью, отображаемые поля,
        подписи к полям и настройки виджетов интерфейса.
        """

        model = Product
        # Модель, с которой связана форма.

        fields = [
            "name",
            "description",
            "category",
            "price",
        ]
        # Список полей модели, включаемых в форму.

        labels = {
            "name": "Название товара",
            "description": "Описание товара",
            "category": "Категория товара",
            "price": "Цена за единицу",
        }
        # Кастомные метки для отображения полей в интерфейсе.

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите наименование товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание товара",
                    "rows": "3",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        """
        Настройка виджетов для отдельных полей формы:
        - name: текстовое поле с подсказкой и CSS‑классом для стилизации;
        - description: текстовая область с подсказкой, высотой в 3 строки
          и CSS‑классом;
        - category: выпадающий список с CSS‑классом для единообразного стиля.
        """

    def clean_name(self):
        """
        Кастомный метод валидации для поля 'name'.

        Проверяет, что длина введённого названия товара составляет не менее 5 символов.
        Если условие не выполняется, вызывает ошибку валидации.

        Используется механизм Django clean_<field_name> для добавления
        пользовательских правил проверки данных перед сохранением.

        Returns:
            str: Очищенное значение поля 'name', если валидация пройдена.

        Raises:
            ValidationError: Если длина названия меньше 5 символов, с сообщением
                об ошибке на русском языке.
        """
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise ValidationError(
                "Название товара не может быть короче 5 символов"
            )
        return name
