from django.contrib import admin
from .models import Help, NeedHelp


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    pass


@admin.register(NeedHelp)
class NeedHelpAdmin(admin.ModelAdmin):
    pass

# Register your models here.
