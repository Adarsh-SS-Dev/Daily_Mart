from django.contrib import admin
from .models import Category,Products

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","img","desc")




class ProductsAdmin(admin.ModelAdmin):
    list_display = ("pro","name","img","desc","qty","discount","price","rating","delivery")




admin.site.register(Category , CategoryAdmin)
admin.site.register(Products , ProductsAdmin)
