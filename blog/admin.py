from django.contrib import admin
from .models import Category, Item
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    pass

admin.site.register(Category, CategoryAdmin )
admin.site.register(Item)
