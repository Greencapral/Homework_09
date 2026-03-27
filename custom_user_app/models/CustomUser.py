from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):

    def create_user(
        self, email, password=None, **extra_fields
    ):

        if not email:
            raise ValueError(
                "Без указания email нельзя создать пользователя."
            )

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, password=None, **extra_fields
    ):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email, password, **extra_fields
        )


class CustomUser(AbstractUser):

    username = models.CharField(
        max_length=70,
        unique=False,
        blank=True,
        null=True,
        verbose_name="Имя пользователя.",
    )
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
