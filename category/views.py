from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .forms import ContactForm


# Create your views here.

def home_page(request):
    # https://docs.djangoproject.com/en/1.10/topics/db/queries/
    #return HttpResponse('<h1>Hello World</h1>')
    categories = Category.objects.filter(name__isnull=False, 
                                         category__isnull=True)
    print(categories.query)
    return render(request, 'homepage.html', {'categories':categories})


def products(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'products.html', {'category': category})


def contact(request):
    print(request.POST.get('fullname'))
    form = ContactForm(request.POST)
    return render(request, 'contact.html', {'form': form})
