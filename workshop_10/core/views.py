from django.shortcuts import render
from core.models import Product

# Create your views here.
def home_view(request):
    return render(
        request,
        "index.html",
        {
            "products": Product.objects.all()
        }
    )


def about_view(request):
    return render(request, "about.html")
