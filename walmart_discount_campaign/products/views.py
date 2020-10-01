from django.shortcuts import render
from .models import Product
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def is_palindrome(s):
    return s == s[::-1]

def index(request):
    products = Product.objects.using('promotions').all()
    context = {
        'products': products[:20],
    }
    return render(request, 'index.html', context=context)


def search(request):
    search_term = request.GET.get('search_term', '')
    products = Product.objects.using('promotions').all()
    context = {
        'search_term': search_term,
        'palindrome_dsc': False
    }

    if search_term.isnumeric():
        products_by_id = products.filter(id=search_term)
        if products_by_id:
            context['products'] = [products_by_id[0],]
        return render(request, 'index.html', context=context)

    if len(search_term) < 4:
        context['error'] = 'La búsqueda debe ser de al menos 3 caracteres'
        return render(request, 'index.html', context=context)

    if is_palindrome(search_term):
        context['palindrome_dsc'] = True
    products = products.filter(Q(description__contains=search_term) | Q(brand__contains=search_term))
    context['products'] = products
    return render(request, 'index.html', context=context)