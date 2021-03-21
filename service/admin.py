from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe

from .models import Post, Service  # , Heating, Cooling


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

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(Heating, CustomAdmin)

# admin.site.register(Cooling, CustomAdmin)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 4:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
