from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.reverse import reverse_lazy

from kitchen.forms import (
    CookCreationForm,
    DishTypeSearchForm,
    DishForm,
    CookInfoUpdateForm,
)
from kitchen.models import Cook, Dish, DishType


@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = DishType.objects.all()
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    form_class = DishForm
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dishtype_detail.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.all()
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class CookInfoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookInfoUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")
