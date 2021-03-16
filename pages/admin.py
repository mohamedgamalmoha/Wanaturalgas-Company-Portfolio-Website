from django.contrib import admin

from .models import About, Residential, Finance, ServicesPage


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Residential)
class ResidentialAdmin(admin.ModelAdmin):

    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):

    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):

    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

