from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ShortenerForm, UserRegistrationForm
from .models import Shortener
from .utils import get_short_url


def home(request):
    urls = Shortener.objects.filter(user=request.user)
    site = get_current_site(request)
    form = ShortenerForm()
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.short_url = get_short_url()
            url.save()
            return redirect('home')

    context = {
        'urls': urls,
        'site': site,
        'form': form
    }
    return render(request, 'index.html', context)


def redirect_to_main_url(request, token):
    url = Shortener.objects.get(short_url=str(token))

    if url:
        return redirect(url.long_url)
    else:
        return HttpResponse('Invalid URL')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
