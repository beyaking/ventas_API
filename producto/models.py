from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
class ProductListing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quantity+' '+self.product.name)
    
