from django.core.management import BaseCommand
from faker import Faker
from random import randint, choice

from store_app.models import Product, Category


class Command(BaseCommand):
    """
    Команда управления Django для генерации тестовых данных.

    Создаёт тестовые записи для моделей Category (6 категорий) и Product (20 товаров).
    Используется для наполнения базы данных при разработке и тестировании приложения.
    """

    help = "Генерация тестовых данных для моделей Product и Category"
    """Текст справки, отображаемый при выполнении команды `python manage.py help`."""

    def handle(self, *args, **kwargs):
        """
        Основной метод команды, выполняющий генерацию тестовых данных.

        Алгоритм работы:
        1. Создаёт 6 категорий с предопределёнными названиями.
        2. Генерирует 20 товаров со случайными данными:
           - название (2 случайных слова);
           - цена (случайное число);
           - категория (выбирается случайно из созданных);
           - описание (случайный текст до 150 символов).

        Args:
            *args: Позиционные аргументы командной строки (не используются).
            **kwargs: Именованные аргументы командной строки (не используются).

        Returns:
            None: Метод выводит сообщения в консоль через self.stdout.write,
            но не возвращает значения.
        """
        self.stdout.write("Генерируем категории")
        cat_names = [
            "Продукты питания",
            "Бытовая химия",
            "Товары для дома",
            "Электроника и бытовая техника",
            "Одежда и аксессуары",
            "Спорт и активный отдых",
        ]

        fake = Faker()

        categories = []
        for _ in range(6):
            category = Category.objects.create(
                name=cat_names[_]
            )
            categories.append(category)

        self.stdout.write("Генерируем товары")

        products = []
        for _ in range(20):
            product = Product.objects.create(
                name=" ".join(fake.words(nb=2)),
                price=fake.random_number(randint(1, 3)),
                category=choice(categories),
                description=fake.text(max_nb_chars=150),
            )
            products.append(product)

        self.stdout.write("Генерация закончена")
