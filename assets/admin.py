from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Asset, MaintenanceLog

admin.site.register(Department)

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Department Info', {'fields': ('department',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Department Info', {'fields': ('department',)}),
    )

admin.site.register(User, CustomUserAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'repair_cost', 'assigned_to')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assigned_to":
            field = super().formfield_for_foreignkey(db_field, request, **kwargs)
            field.label_from_instance = lambda obj: f"{obj.username} - ({obj.department.name if obj.department else 'No Dept'})"
            return field
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Asset, AssetAdmin)

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('asset', 'service_date', 'cost', 'description')
    list_filter = ('service_date', 'asset')