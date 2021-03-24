from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Main(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = RichTextField()


class Post(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')
    object_id = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = RichTextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service:post', kwargs={'post_id': self.id})


class Heating(Main):

    class Meta:
        verbose_name = 'Heating'
        verbose_name_plural = 'Heating'

    def __str__(self):
        return self.title


class Cooling(Main):

    class Meta:
        verbose_name = 'Cooling'
        verbose_name_plural = 'Cooling'

    def __str__(self):
        return self.title


class Service(models.Model):
    image = models.ImageField(upload_to='images/services/', null=True)
    title = models.CharField(max_length=250)
    description = RichTextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
