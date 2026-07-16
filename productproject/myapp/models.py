from django.db import models

# Create your models here.
class Products(models.Model):
    pname = models.CharField(max_length=50)
    price = models.IntegerField()
    ptype = models.CharField()
    p_mgf = models.DateField()
    p_exp = models.DateField()


    def __str__(self):
        return self.pname