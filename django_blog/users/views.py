from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Post
from django.core.paginator import Paginator


# Log actions of django
import logging
log = logging.getLogger(__name__)


# Create your views here.
def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # Check if all field of form is valided
        if form.is_valid():
            fs = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # Check password
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'That email is being used')
                        return redirect('register')
                    else:
                      # Look good
                        fs.save()
                        user = auth.authenticate(
                            username=username, password=password1)
                        auth.login(request, user)
                        fs.user = request.user
                        messages.success(
                            request, 'Account created for ' + username)
                        return redirect('home')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('register')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')
    return


@login_required
def profile(request, user_slug):
    # user_profile = Profile.objects.get(user__username=user_slug)
    userFound = get_object_or_404(User, username=user_slug)
    posts = Post.objects.filter(author=userFound).order_by('-created_at')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    if userFound is not None:
        context = {
            'user_view': userFound,
            'posts': paged_posts
        }
        return render(request, 'users/profile.html', context)
    else:
        context = {
            'posts': paged_posts
        }
        return render(request, 'users/profile.html', context)


@login_required
def editProfile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('editProfile')

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render(request, 'users/editProfile.html', context)
