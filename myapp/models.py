from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.models.CharField(max_length=50, unique=true, verbose_name = 'Nombre')
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class tag(models.Model):
    name = models.models.CharField(max_length=50, unique=true, verbose_name = 'Nombre')
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Catalogue(models.Models):
    title = models.models.CharField(max_length=50, verbose_name = 'titulo')
    description = models.models.TextField(verbose_name = 'descripcion')
    image = models.models.ImageField(upload_to='catalogue', verbose_name = 'imagen')
    created = models.models.CharField(max_length=4, verbose_name = 'Año de estreno')
    studio = models.models.CharField(max_length=50, verbose_name = 'Estudio')
    episode = models.models.models.IntegerField(max_lengt=5, verbose_name = 'Episodios')
    seasson = models.models.models.IntegerField(max_lengt=5, verbose_name = 'Temporadas')
    language = models.models.CharField(max_length=50, verbose_name = 'Idiomas')
    caption = models.models.CharField(max_length=50, verbose_name = 'Subtitulos')
    #relacionales
    category = models.models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.models.ForeignKey(tag, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Catalogue")
        verbose_name_plural = _("Catalogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    
    
