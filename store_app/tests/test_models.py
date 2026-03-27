import pytest
from store_app.models import Category, Product


@pytest.mark.django_db
class TestCategoryCRUD:
    def test_category_creation(self,category_1):
        """Тест создания категории."""
        assert Category.objects.count() == 1

    def test_read_category(self,category_1):
        """Тест чтения категории."""
        retrieved_category = Category.objects.get(pk=category_1.pk)
        assert retrieved_category.name == "Тестовая категория"

    def test_update_category(self,category_1):
        """Тест обновления категории."""
        category = Category.objects.get(name="Тестовая категория")
        category.name = "Тестовая категория 2"
        category.save()
        updated_category = Category.objects.get(pk=category_1.pk)
        assert updated_category.name == "Тестовая категория 2"

    def test_delete_category(self,category_1):
        """Тест удаления категории."""
        category_id = category_1.pk
        category_1.delete()
        with pytest.raises(Category.DoesNotExist):
            Category.objects.get(pk=category_id)


@pytest.mark.django_db
class TestProductCRUD:
    def test_product_creation(self,product_1):
        """Тест создания продукта."""
        assert Product.objects.count() == 1

    def test_read_product(self,product_1):
        """Тест чтения продукта."""
        retrieved_product = Product.objects.get(name=product_1.name)
        assert retrieved_product.price == 33.33

    def test_update_product(self,product_1):
        """Тест обновления продукта."""
        product = Product.objects.get(price=product_1.price)
        product.name = "тестовый продукт №2"
        product.save()
        updated_product = Product.objects.get(price=product_1.price)
        assert updated_product.name == "тестовый продукт №2"

    def test_delete_product(self,product_1):
        """Тест удаления продукта."""
        product_id = product_1.pk
        product_1.delete()
        with pytest.raises(Product.DoesNotExist):
            Product.objects.get(pk=product_id)
