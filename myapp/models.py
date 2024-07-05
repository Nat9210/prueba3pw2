from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Categoria')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})