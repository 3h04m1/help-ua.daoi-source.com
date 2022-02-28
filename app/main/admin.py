from django.contrib import admin
from .models import Help, NeedHelp


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'address',
        'name',
        'tel',
        # 'pub_date',
        'mod_date'
        )
    list_filter = (
        'address',
        'category',
    )
    search_fields = (
        'title',
        'address',
        'name',
        'tel',
        'category',
    )
    


@admin.register(NeedHelp)
class NeedHelpAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        # 'address',
        'category',
        'name',
        'tel',
        'pub_date',
        'mod_date'
        )
    list_filter = (
        # 'address',
        'category',
        'title',
    )
    search_fields = (
        'title',
        # 'address',
        'category',
        'name',
        'tel',
    )
    

# Register your models here.
