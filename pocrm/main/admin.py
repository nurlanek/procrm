from django.contrib import admin
from .models import Kroy_detail, Kroy
from django.utils.safestring import mark_safe


# Register your models here.
class KroyAdmin(admin.ModelAdmin):
    list_display = ("kroy_no","name", "ras_tkani", "ras_dublerin", "edinitsa", "description", "created", "is_active",)
    search_fields = ("kroy_no",)
    list_editable = ("is_active",)

class Kroy_detailAdmin(admin.ModelAdmin):
    list_display = ("kroy", "pachka", "razmer", "rost", "stuk" )
    search_fields = ("kroy",)


admin.site.register(Kroy, KroyAdmin)
admin.site.register(Kroy_detail, Kroy_detailAdmin)