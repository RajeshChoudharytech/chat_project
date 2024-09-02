from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ChatListView,
    ChatDetailView,
    CreateGroupChatView,
)

urlpatterns = [
    # Chat URLs
    path('', ChatListView.as_view(), name='chat_list'),  # List of all chats
    path('chat/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),  # Detail view for a specific chat
    # path('chat/<int:pk>/edit/<int:message_id>/', MessageEditView.as_view(), name='edit_message'),  # Edit message

    # Group Chat URLs
    path('group/create/', CreateGroupChatView.as_view(), name='group_chat_create'),  # Create group chat
    # path('group/<int:pk>/', GroupChatDetailView.as_view(), name='group_chat_detail'),  # Detail view for a group chat
]
