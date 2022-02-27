from django.contrib import admin
from .models import Help, NeedHelp


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = (
        'help_type',
        'address',
        'name',
        'tel',
        'pub_date',
        'mod_date'
        )
    list_filter = (
        'address',
        'help_type',
    )
    search_fields = (
        'help_type',
        'address',
        'name',
        'tel',
    )
    


@admin.register(NeedHelp)
class NeedHelpAdmin(admin.ModelAdmin):
    list_display = (
        'help_type',
        # 'address',
        'name',
        'tel',
        'pub_date',
        'mod_date'
        )
    list_filter = (
        # 'address',
        'help_type',
    )
    search_fields = (
        'help_type',
        # 'address',
        'name',
        'tel',
    )
    

# Register your models here.
