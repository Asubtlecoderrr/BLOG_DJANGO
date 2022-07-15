from django.contrib import admin
from .models import Post,Category,Tag,CustomUser
from .models import Post, Comment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username","first_name","last_name","email")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title","created_date","published_date",'image')
    list_filter = ('published_date',)
    view_on_site = True
    def view_on_site(self,obj):
        from django.urls import reverse
        return reverse('blog:post_detail',kwargs={'slug':obj.slug})
    
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_date")
    list_filter = ('created_date',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name","created_date")
    list_filter = ('created_date',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created_on','post')
    list_filter = ('created_on',)

