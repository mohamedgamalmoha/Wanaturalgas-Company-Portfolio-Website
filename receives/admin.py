from django.contrib import admin
from .models import Contact, MainRequests


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (('Main Info', {'fields': ('first_name', 'last_name', 'emil_address', 'phone_number', 'zip_code',
                                           'Question'
                                           )}),)

    list_display = ['__str__']

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]


@admin.register(MainRequests)
class MainRequestsAdmin(admin.ModelAdmin):
    fieldsets = (('Main Info', {'fields': (
        'request_id', 'q1', 'home_temperature', 'field_of_interest', 'issue_of_concern', 'equipment_age', 'first_name',
        'last_name', 'email', 'contact_phone', 'cell_phone', 'street_address', 'address_line_2', 'wa', 'city',
        'zip_code'
    )}),)

    list_display = ['__str__']

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

