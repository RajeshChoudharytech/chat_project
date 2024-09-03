from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["participant","is_group_chat", "created_at"]

admin.site.register(Message)
admin.site.register(UnreadMessage)

