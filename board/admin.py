from django.contrib import admin
from .models import  UserProfile, Category, Ad, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('category', 'is_active')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad', 'user', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment, CommentAdmin)











