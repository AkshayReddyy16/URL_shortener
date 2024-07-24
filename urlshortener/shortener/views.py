# shortener/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import random
import string

url_map = {}

def generate_short_code():
    characters = string.digits + string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(5))

def home(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_code = generate_short_code()
        # Handle collision
        while short_code in url_map:
            short_code = generate_short_code()
        url_map[short_code] = long_url
        URL.objects.create(long_url=long_url, short_code=short_code)
        return render(request, 'shortener/home.html', {'short_url': request.build_absolute_uri('/') + short_code})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    long_url = url_map.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        url = get_object_or_404(URL, short_code=short_code)
        return redirect(url.long_url)
