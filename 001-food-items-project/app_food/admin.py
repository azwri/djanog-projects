from django.contrib import admin
from . import models

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at', 'is_deleted')
    ordering = ('-created_at',)
    list_editable = ('price', 'is_deleted')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_deleted',)
        }),
    )