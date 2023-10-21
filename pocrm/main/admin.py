from django.contrib import admin
#from .models import Work_stations, Category, Article, Master_data, Testmodel
from django.utils.safestring import mark_safe


# Register your models here.

"""class Work_stationsAdmin(admin.ModelAdmin):
    list_display = ("work_station", "is_active", "category", "employee_name", "slug",)
    list_editable = ("is_active",)
    search_fields = ("work_station", "description",)
    readonly_fields = ("slug",)
    list_filter = ("is_active", "category",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    #list_editable = ("",)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    #list_editable = ("",)

class Master_dataAdmin(admin.ModelAdmin):
        list_display = ("quantity", "article", "work_stations", "category", "created")
        # list_editable = ("",)


class TestmodelAdmin(admin.ModelAdmin):
    list_display = ("ws1", "ws2")
    # list_editable = ("",)

admin.site.register(Work_stations, Work_stationsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Master_data, Master_dataAdmin)
admin.site.register(Testmodel, TestmodelAdmin)
"""