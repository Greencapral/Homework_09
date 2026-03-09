from django.forms import ModelForm
from django.core.exceptions import ValidationError
from store_app.models import Category


class CategoryForm(ModelForm):
    """
    Форма для создания и редактирования категорий товаров.

    Наследует ModelForm для автоматической генерации полей на основе модели Category.
    Содержит кастомную валидацию поля name — проверяет, что длина названия
    не менее 5 символов.
    """

    class Meta:
        """
        Метаданные формы, определяющие связь с моделью и настройки отображения.
        """

        model = Category
        # Модель, с которой связана форма.

        fields = [
            "name",
            "description",
        ]
        # Список полей модели, включаемых в форму.

        labels = {
            "name": "Название категории",
            "description": "Описание категории",
        }
        # Кастомные метки для отображения полей в интерфейсе.

    def clean_name(self):
        """
        Кастомный метод валидации для поля 'name'.

        Проверяет, что длина введённого названия категории составляет не менее 5 символов.
        Если условие не выполняется, вызывает ошибку валидации.

        Returns:
            str: Очищенное значение поля 'name', если валидация пройдена.

        Raises:
            ValidationError: Если длина названия меньше 5 символов.
        """
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise ValidationError(
                "Название категории не может быть короче 5 символов"
            )
        return name
