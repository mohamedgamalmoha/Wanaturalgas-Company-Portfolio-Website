from django.db import models
from ckeditor.fields import RichTextField


class Core(models.Model):
    title = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    description = RichTextField()


class About(Core):

    class Meta:
        verbose_name = 'About Us Page'
        verbose_name_plural = 'About Us Page'

    def __str__(self):
        return self.title


class Residential(Core):

    class Meta:
        verbose_name = 'Residential Page'
        verbose_name_plural = 'Residential Page'

    def __str__(self):
        return self.title


class Finance(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/Finance/')
    description = RichTextField()

    class Meta:
        verbose_name = 'Financing Page'
        verbose_name_plural = 'Financing Page'

    def __str__(self):
        return self.title
