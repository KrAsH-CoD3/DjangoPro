from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self) -> str:
        return self.name
    
    # The variables below is the `id` and `name` in the each of the form values which should be the same.
    # The `id` and `name` must have the variable name. IT A MUST.
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')