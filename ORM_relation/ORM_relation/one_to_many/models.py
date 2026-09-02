from django.db import models

# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=100)



    def __str__(self):
        return self.cname

class Product(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    Category=models.ForeignKey(
        Category,on_delete=models.CASCADE
    )

    def __str__(self):
        return self.pname


