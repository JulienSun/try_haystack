from django.contrib import admin
from knowledge.models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
