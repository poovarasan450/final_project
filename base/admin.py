from django.contrib import admin
from base.models import Category,Articles

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','created_at']
    
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','category','updated_at','status','is_treanding']
    prepopulated_fields={
        'slug':('title',)
        }

admin.site.register(Category,CategoryAdmin)
admin.site.register(Articles,ArticleAdmin)