from django.contrib import admin
from .models import Topic, Post, Comment

def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = 'Mark as published'

def make_draft(modelsadmin, request, queryset):
    queryset.update(status='draft')
make_draft.short_description = 'Mark as draft'

# admin.site.register(Topic)
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
    actions = [make_published, make_draft]
    
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','topic', 'slug', 'publish', 'status') #'author',
    list_filter = ('status', 'created', 'publish') #, 'author'
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    actions = [make_published, make_draft]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')