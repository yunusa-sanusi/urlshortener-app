from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ShortenerForm
from .models import Shortener
from .utils import get_short_url


def home(request):
    urls = Shortener.objects.all()
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
    url = Shortener.objects.get(short_url=token)

    if url:
        return redirect(url.long_url)
    else:
        return HttpResponse('Invalid URL')
