from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title =models.CharField(max_length=50)
    description=models.TextField(max_length=350)
    image=models.ImageField(upload_to='images/',blank=True)
    url=models.URLField(blank=True)
    video=models.FileField(upload_to='videos/',blank=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title