from django.contrib import admin
from .models import *


admin.site.register(Wateroff)
admin.site.register(Cities)
admin.site.register(Menuitem)

class PostAdminManager(admin.ModelAdmin):
    readonly_fields = ['slug']
admin.site.register(Post, PostAdminManager)

class CategoryAdminManager(admin.ModelAdmin):
    readonly_fields = ['slug']
admin.site.register(Category, CategoryAdminManager)
