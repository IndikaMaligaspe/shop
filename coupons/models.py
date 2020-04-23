from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Coupon(models.Model):
    code = models.CharField( max_length=50, unique=True)
    valid_from = models.DateTimeField(auto_now=False, auto_now_add=False)
    valid_to = models.DateTimeField(auto_now=False, auto_now_add=False)
    discount = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()


    def __str__(self):
        return self.code

    # def get_absolute_url(self):
    #     return reverse("Coupons_detail", kwargs={"pk": self.pk})

