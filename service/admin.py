from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import Heating, Cooling, Post, Service


class PostInline(GenericTabularInline):
    model = Post

    def show_image(self, obj):

        return mark_safe(

            (
                f"<a href='{obj.image.url}' >\n"
                f"<img src='{obj.image.url}' width={150} height={200}>\n"
                f"</a>"
            )
        )


class CustomAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]


admin.site.register(Heating, CustomAdmin)

admin.site.register(Cooling, CustomAdmin)

admin.site.register(Service)
