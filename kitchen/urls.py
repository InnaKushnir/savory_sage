from django.urls import path

from kitchen.views import (
    index,
    CookDetailView,
    CookListView,
    CookCreateView,
    CookInfoUpdateView,
    CookDeleteView,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishTypeDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookInfoUpdateView.as_view(), name="cook-update"), # noqa
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"), # noqa
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"), # noqa
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"), # noqa
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"), # noqa
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"), # noqa
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
]

app_name = "kitchen"
