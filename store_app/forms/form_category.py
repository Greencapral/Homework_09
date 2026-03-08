from django.forms import ModelForm
from django.core.exceptions import ValidationError
from store_app.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description",
        ]
        labels = {
            "name": "Название категории",
            "description": "Описание категории",
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise ValidationError(
                "Название категории не может быть короче 5 символов"
            )
        return name
