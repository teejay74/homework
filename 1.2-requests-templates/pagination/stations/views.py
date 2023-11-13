from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
from .utils import load_csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    all_stations = load_csv()

    paginator = Paginator(all_stations, 10)
    page = request.GET.get('page')

    try:
        stations = paginator.page(page)
    except PageNotAnInteger:
        stations = paginator.page(1)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
