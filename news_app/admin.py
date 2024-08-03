from django.contrib import admin
from .models import News, Category, Contact
# admin.site.register(News)
# admin.site.register(Category)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'category', 'status']
    list_filter = ['title', 'publish_time','created_time']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    date_hierarchy = 'publish_time'
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Contact)