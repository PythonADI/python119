from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
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


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = "core/product_details.html"


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    fields = "__all__"
    template_name = "core/product_create.html"

    def get_success_url(self):
        return reverse("core:product-details", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    fields = "__all__"
    template_name = "core/product_update.html"

    def get_success_url(self):
        return reverse("core:product-details", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = "core/product_delete.html"
    success_url = reverse_lazy("core:home")
