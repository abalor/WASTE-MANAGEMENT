from django.contrib import admin
from .models import *

# @admin.register(WasteImage)
class WasteImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')  # Use valid fields from the model


admin.site.register(WasteImage, WasteImageAdmin)



# class WasteImageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user', 'created_at')  # Show name, uploader, and created date
#     list_filter = ('user', 'created_at')          # Add filters for easier management
#     search_fields = ('name', 'description')       # Enable searching by name and description

# admin.site.register(WasteImage, WasteImageAdmin)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'image', 'text', 'created_at')  # Show user, image, and comment details
#     list_filter = ('created_at',)                           # Filter by created date
#     search_fields = ('text',)                               # Enable searching by comment text

# admin.site.register(Comment, CommentAdmin)
