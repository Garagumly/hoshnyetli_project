from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.shortcuts import render, get_object_or_404
from django.utils import translation
from . models import *
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.utils.translation import get_language, activate, gettext

# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


def products(request):
    return render(request, "store/products_page.html", {"products": Product.objects.all()})


def product_detail_titiz(request, id):
    identified_product = get_object_or_404(Product, pk=id)
    related_product = Product.objects.filter(
        category=identified_product.category).exclude(id=id)[:4]
    return render(request, "store/product_detail_titiz.html", {
        "product": identified_product,
        "related_product": related_product,
        #   "post_tags": identified_product.tags.all()
    })


def product_detail_rorax(request, id):
    identified_product = get_object_or_404(Product, pk=id)
    related_product = Product.objects.filter(
        category=identified_product.category).exclude(id=id)[:4]
    return render(request, "store/product_detail_titiz.html", {
        "product": identified_product,
        "related_product": related_product,
        #   "post_tags": identified_product.tags.all()
    })


def product_detail_modaline(request, id):
    identified_product = get_object_or_404(Product, pk=id)
    related_product = Product.objects.filter(
        category=identified_product.category).exclude(id=id)[:4]
    return render(request, "store/product_detail_titiz.html", {
        "product": identified_product,
        "related_product": related_product,
        #   "post_tags": identified_product.tags.all()
    })


def products_titiz(request):
    products_titiz = Product.objects.filter(brand__name="Titiz")    
    product_filter = ProductFilter(request.GET, queryset=products_titiz)
    titiz_paginator = Paginator(product_filter.qs, 18) 
    page_list = request.GET.get('page')
    page = titiz_paginator.get_page(page_list)
    category = Category.objects.all().exclude(name="auto cleaning products")
    brand = request.GET.get('brand')
    category = request.GET.get('category')

    if is_valid_queryparam(category) and category != 'Choose...':
        products_titiz = products_titiz.filter(category__name=category)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        products_titiz = products_titiz.filter(brand__name=brand)

    context = {
        "count" : titiz_paginator.count,
        # "page" : page,
        "page" : page,
        "filtered_prodcuts" : product_filter.qs,
        'from' : product_filter.form,
        "products_titiz": products_titiz,
        "cats": Product.objects.distinct().values('category__name', 'category__id').exclude(category__name="auto cleaning products"),
        'brands': Product.objects.distinct().values('brand__name', 'brand__id')
    }
    return render(request, "store/products_titiz.html", context)


def products_rorax(request):
    products_rorax = Product.objects.filter(brand__name="Rorax")
    category = Product.objects.filter(category__name='auto cleaning products')
    category = request.GET.get('category')

    if is_valid_queryparam(category) and category != 'Choose...':
        products_rorax = products_rorax.filter(category__name=category)

    context = {
        "products_rorax": products_rorax,
        "cats": category,
        'brands': Product.objects.distinct().values('brand__name', 'brand__id')
    }
    return render(request, "store/products_rorax.html", context)


def products_modaline(request):
    products_modaline = Product.objects.filter(brand__name="Modaline")
    category = Product.objects.filter(category__name='Modaline')
    category = request.GET.get('category')

    if is_valid_queryparam(category) and category != 'Choose...':
        products_modaline = products_modaline.filter(category__name=category)

    context = {
        "products_modaline": products_modaline,
        "cats": category,
        'brands': Product.objects.distinct().values('brand__name', 'brand__id')
    }
    return render(request, "store/products_modaline.html", context)


def index(request):
    context = {}
    return render(request, "store/index.html", context)


def try_page(request):
    context = {}
    return render(request, "store/try_page.html", context)


def store(request):
    titiz_products_3 = Product.objects.filter(brand__name="Titiz")[:3]
    rorax_products_3 = Product.objects.filter(brand__name="Rorax")[:3]
    modaline_products_3 = Product.objects.filter(brand__name="Modaline")[:3]

    context = {
        "titiz_products_3": titiz_products_3,
        "rorax_products_3": rorax_products_3,
        "modaline_products_3": modaline_products_3
    }
    return render(request, "store/store.html", context)


def about(request):
    context = {}
    return render(request, "store/about.html", context)


def brands(request):
    latest_posts = Product.objects.all()
    context = {}
    return render(request, "store/brands.html", {
        "posts": latest_posts
    })


def contacts(request):
    context = {}
    return render(request, "store/contacts.html", context)

def check(request):
    languages = []
    if request.method == 'POST':
        languages = request.POST.getlist('languages')
    return render(request, 'checkbox.html',{'languages':languages})


def services(request):
    context = {}
    return render(request, "store/services.html", context)


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
