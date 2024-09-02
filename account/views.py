from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from .models import UserProfile


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        profile_form = UserProfileForm(self.request.POST, self.request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = self.object
            profile.save()
        return response

    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            breakpoint()
            if user is not None:
                login(request, user)
                return redirect('chat_list')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})