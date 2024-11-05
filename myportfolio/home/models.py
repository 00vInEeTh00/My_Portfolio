from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title =models.CharField(max_length=50,null=False)
    description=models.TextField(max_length=350,null=False)
    url=models.URLField(blank=True,null=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    video=models.FileField(upload_to='videos/',blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title