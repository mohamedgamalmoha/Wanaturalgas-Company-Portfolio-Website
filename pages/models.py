from django.db import models
from ckeditor.fields import RichTextField


class Core(models.Model):
    title = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    description = RichTextField()


class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='pages/about/')
    image_2 = models.ImageField(upload_to='pages/about/')
    image_3 = models.ImageField(upload_to='pages/about/')
    image_4 = models.ImageField(upload_to='pages/about/')
    section_1 = RichTextField()
    section_2 = RichTextField()

    class Meta:
        verbose_name = 'About Us Page'
        verbose_name_plural = 'About Us Page'

    def __str__(self):
        return self.title


class ResidentialPage(models.Model):
    title = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='pages/residential/')
    image_2 = models.ImageField(upload_to='pages/residential/')
    image_3 = models.ImageField(upload_to='pages/residential/')
    image_4 = models.ImageField(upload_to='pages/residential/')
    section_1 = RichTextField()
    section_2 = RichTextField()

    class Meta:
        verbose_name = 'Residential Page'
        verbose_name_plural = 'Residential Page'

    def __str__(self):
        return self.title


class ServicesPage(Core):

    class Meta:
        verbose_name = 'Services Page'
        verbose_name_plural = 'Services Page'

    def __str__(self):
        return self.title


class Finance(models.Model):
    title = models.CharField(max_length=250)
    header_image = models.ImageField(upload_to='pages/finance/', null=True)
    image_2 = models.ImageField(upload_to='pages/finance/', null=True)
    description = RichTextField()

    class Meta:
        verbose_name = 'Financing Page'
        verbose_name_plural = 'Financing Page'

    def __str__(self):
        return self.title
