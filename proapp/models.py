from django.db import models

# Create your models here.

class product(models.Model):
    category = (
        ('Textile','Textile'),
        ('Furniture','Furniture'),
        ('Leather','Leather')
    )
    name = models.CharField(max_length= 200, null = True)
    price = models.IntegerField()
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    category = models.CharField(choices = category, max_length= 10)

    def __str__(self):
        return self.name

    