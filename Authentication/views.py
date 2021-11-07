from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from .models import Profile, comments
from .forms import PasswordChangingForm, UserProfileForm, ProfileForm


def home(request):
    return render(request, 'main_page/index.html')


def github(request):
    return redirect('https://github.com/bl4cknull')


def facebook(request):
    return redirect('https://www.facebook.com/zerobl4ck')


def twitter(request):
    return redirect('https://twitter.com/SefreSiah')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                return render(request, 'authentication/register.html', {'user_valid': 'Username already exists'})

            if User.objects.filter(email=email).exists():
                return render(request, 'authentication/register.html', {'email_valid': 'Email already registered'})

            User_data = User.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            User_data.save()

            return redirect('/login')
        else:
            return render(request, 'authentication/register.html', {'pass_valid': 'Passwords does not match'})
    else:
        return render(request, 'authentication/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_data = auth.authenticate(username=username, password=password)

        if user_data is not None:
            auth.login(request, user_data)
            return redirect('/home')
        else:
            return render(request, 'authentication/login.html', {'valid': 'Your username or password is wrong.'})

    return render(request, 'authentication/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')


@login_required
def profile(request):
    if request.method == 'POST':
        user_data = User.objects.filter(request.POST['username'])

        print(user_data)
    return render(request, 'profile/profile.html')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('logout')


class UserChangeProfile(generic.UpdateView):
    form_class = UserProfileForm
    template_name = 'profile/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


def send_message(request):
    if request.method == 'POST':
        message_context = request.POST['message']
        user = request.user
        comments.objects.create(message=message_context, user=user)
        return render(request, 'main_page/index.html', {'context': 'Your Email sended'})
