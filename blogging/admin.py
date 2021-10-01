from django.contrib import admin
from blogging.models import Post, Catagory

class CatagoryInline(admin.TabularInline):
    model = Catagory.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CatagoryInline,]

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
