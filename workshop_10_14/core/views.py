import random
from string import ascii_lowercase

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Product

@login_required
def home_view(request):
    return render(
        request,
        "index.html",
        {
            "products": Product.objects.all()
        }
    )

@login_required
def about_view(request):
    return render(request, "about.html")

# @login_required
# def product_details_view(request, pk):
#     product = Product.objects.get(pk=pk)
#     return render(request, "core/product_details.html", {
#         "product": product
#     })

@login_required
def generate_random_product_view(request):
    Product.objects.create(
        thumbnail="/products/samsung-galaxy-s25-ultra-titanium-silver-blue.webp",
        name="".join(random.choices(ascii_lowercase, k=20)),
        description="".join(random.choices(ascii_lowercase, k=100)),
        price=random.randint(10, 2000),
        discount=random.randint(0, 100),
        stock=random.randint(0, 100),
    )

    return redirect("core:home")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "core/product_details.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "core/product_create.html"

    def get_success_url(self):
        return reverse("core:product-details", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "core/product_update.html"

    def get_success_url(self):
        return reverse("core:product-details", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "core/product_delete.html"
    success_url = reverse_lazy("core:home")


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 6
    ordering = ["-created_at"]
    search_fields = ["name"]

    def get_queryset(self):
        return super().get_queryset().filter(name__icontains=self.request.GET.get("search", ""))
