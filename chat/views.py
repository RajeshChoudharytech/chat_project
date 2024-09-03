from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from .models import Conversation, Message, UnreadMessage


class ChatListView(LoginRequiredMixin, ListView):
    model = Conversation
    template_name = 'chat_list.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        return self.request.user.conversations.all()


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = Conversation
    template_name = 'chat_detail.html'
    context_object_name = 'conversation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.messages.all()
        return context

    def post(self, request, *args, **kwargs):
        conversation = self.get_object()
        content = request.POST.get('message')
        if content:
            message = Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content,
            )
            # Mark as unread for other participants
            for participant in conversation.participants.exclude(id=request.user.id):
                UnreadMessage.objects.create(user=participant, message=message)
        return redirect('chat_detail', pk=conversation.id)


class CreateGroupChatView(LoginRequiredMixin, CreateView):
    model = Conversation
    fields = []
    template_name = 'create_group_chat.html'
    success_url = reverse_lazy('chat_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        participant_ids = self.request.POST.getlist('participants')
        participants = User.objects.filter(id__in=participant_ids)
        self.object.participants.set(participants)
        self.object.is_group_chat = True
        self.object.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(id=self.request.user.id)
        return context
