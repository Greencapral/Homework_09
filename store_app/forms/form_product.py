from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from store_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
        ]
        labels = {
            "name": "Название товара",
            "description": "Описание товара",
            "category": "Категория товара",
            "price": "Цена за единицу",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "введите наименование товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "введите описание товара",
                    "rows": "3",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise ValidationError(
                "Название товара не может быть короче 5 символов"
            )
        return name
