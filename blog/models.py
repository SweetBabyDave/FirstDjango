from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    content = models.TextField()
    posted = models.DateTimeField()
    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=32)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField()
    def __str__(self):
        return self.commenter