from django.contrib import admin
from core.models import Product, Review

# Register your models here.
# admin.site.register([Product])

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name"]
    list_filter = ["name"]

    readonly_fields = ["created_at", "updated_at"]

admin.site.register(Review)
