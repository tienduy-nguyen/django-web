from django.contrib import admin
from .models import Post, Category
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published',
                    'created_at',)
    list_display_links = ('id', 'title', 'author', )
    list_per_page = 25
    list_filter = ('author', 'tags',)
    search_fields = ('title', 'author', 'tags', 'slug')
    list_editable = ('is_published',)

    def category_name(self, obj):
        return obj.category.title
    category_name.admin_order_field = 'category'  # Allows column order sorting
    category_name.short_description = 'Category Name'  # Renames column head


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
