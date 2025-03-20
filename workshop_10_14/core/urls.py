from django.urls import path
from core.views import (
    about_view,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,
    generate_random_product_view
)

app_name = "core"

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("about/", about_view, name="about"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("products/generate/", generate_random_product_view, name="generate-random-product"),
]
