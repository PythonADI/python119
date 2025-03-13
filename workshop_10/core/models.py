from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Product(models.Model):
    thumbnail = models.ImageField(upload_to="products/", blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        default=0.00,
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(100.00)]
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0.0

    def get_stars(self):
        half_star = '<i class="bi bi-star-half text-warning"></i>' * (self.rating() % 1 > 0)
        full_stars = '<i class="bi bi-star-fill text-warning"></i>' * int(self.rating())
        if half_star:
            return full_stars + half_star + '<i class="bi bi-star text-warning"></i>' * (5 - int(self.rating()) - 1)

        return full_stars +  '<i class="bi bi-star text-warning"></i>' * (5 - int(self.rating()))


class Review(models.Model):
    class Meta:
        unique_together = ["user", "product"]

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
