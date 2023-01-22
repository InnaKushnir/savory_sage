from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return f"{self.name} ({self.dish_type}) : {self.price}"
