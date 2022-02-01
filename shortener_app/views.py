from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ShortenerForm
from .models import Shortener
from .utils import get_short_url


def home(request):
    urls = Shortener.objects.all()
    return render(request, 'index.html', {'urls': urls, 'site': get_current_site(request)})


def create_short_url(request):
    site = get_current_site(request)
    form = ShortenerForm()
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.short_url = get_short_url(site)
            url.save()
            return redirect('home')

    return render(request, 'create_short_url.html', {'form': form})


def redirect_to_main_url(self, short_url):
    url = Shortener.objects.get(short_url=short_url)
    url.count = url.count + 1
    url.save()

    if url:
        return redirect(f'{url.long_url}')
    else:
        return HttpResponse('Invalid URL')
