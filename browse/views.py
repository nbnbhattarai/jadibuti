from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


# Create your views here.

def herbs_list(response):

    herbs = Herb.objects.all().order_by('eng_name')
    total_herbs = herbs.count()
    herb_categories = HerbCategory.objects.all()

    context = {
        'page_title': 'Herbs',
        'herbs': herbs,
        'total_herbs': total_herbs,
        'categories': herb_categories,
    }

    return render(response, 'browse_herbs.html', context)


def yoga_list(response):

    yogas = Yoga.objects.all()

    context = {
        'page_title': 'Yoga',
        'yogas': yogas,
    }

    return render(response, 'browse_yogas.html', context)


def yoga_detail(response, id=None):

    yoga = get_object_or_404(Yoga, id=id)

    context = {
        'page_title': 'Yoga',
        'yoga': yoga,
    }

    return render(response, 'yoga_detail.html', context)


def herb_detail(response, slug):

    herb = get_object_or_404(Herb, id=slug)
    shops = herb.shops.all()
    diseases_cured = herb.disease_set.all()

    context = {
        'page_title': 'herb_detail',
        'herb': herb,
        'available_in': shops,
        'diseases_cured': diseases_cured
    }

    return render(response, 'herb_detail.html', context)


def shop_detail(response, slug):

    shop = get_object_or_404(HerbShop, id=slug)
    available_herbs = shop.herb_set.all()

    context = {
        'page_title': shop.name,
        'shop': shop,
        'available_herbs': available_herbs,
    }

    return render(response, 'shop_detail.html', context)


def browse_view(response):

    herbs = Herb.objects.all()

    context = {
        'page_title': 'Herbs',
        'herbs': herbs
    }

    return render(response, 'browse_herbs.html', context)
