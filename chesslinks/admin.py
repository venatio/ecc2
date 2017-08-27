from django.contrib import admin

from .models import Category
from .models import Link


#admin.site.register(Link)
#admin.site.register(Category)

class LinkInline(admin.TabularInline):
    model = Link
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    fields = ['Name']
    inlines = [LinkInline]


admin.site.register(Category, CategoryAdmin)
# Register your models here.
