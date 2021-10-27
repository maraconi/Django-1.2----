from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import os, csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    path = os.path.abspath('data-398-2018-08-30.csv')
    with open(path, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)
        bus_stations = list()
        for i in data:
            station = {'Name': i['Name'],
                       'Street': i['Street'],
                       'District': i['District']}
            bus_stations.append(station)
    page_number = request.GET.get('page', 1)
    elements_per_page = 13
    paginator = Paginator(bus_stations, elements_per_page)
    page = paginator.get_page(page_number)
    content = page.object_list
    context = {
        'bus_stations': content,
        'page': page
    }
    return render(request, 'stations/index.html', context)
