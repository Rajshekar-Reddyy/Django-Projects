from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=30)
    created_at=models.DateField()


    def __str__(self):
        return self.title 