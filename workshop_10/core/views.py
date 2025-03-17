from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

@login_required
def product_details_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product_details.html", {
        "product": product
    })
