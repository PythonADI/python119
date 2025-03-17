from django.urls import path
from core.views import (
    home_view,
    about_view,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "core"

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),

]
