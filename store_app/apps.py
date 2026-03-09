from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    """
    Конфигурация приложения Django для модуля store_app.

    Класс определяет базовую конфигурацию приложения, необходимую для его корректной
    интеграции в проект Django. Используется системой приложений Django при запуске
    и инициализации компонентов проекта.
    """

    name = "store_app"
