from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    

class Moview(models.Model):
    movie = models.CharField(max_length=50)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie + " (" + str(self.year) + ")"


class Comment(models.Model):
    user = models.CharField(max_length=70)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   

    def __str__(self):
        return self.user 
