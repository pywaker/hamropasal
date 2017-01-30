from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Category
from .forms import ContactForm, CategoryForm, ProductForm


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
    form = ContactForm(request.POST or None)
    print(form.is_valid(), form.data, form.cleaned_data)
    return render(request, 'contact.html', {'form': form})


def list_category(request):
    pass


#def add_category(request):
    #form = CategoryForm(request.POST or None)
    #form.fields['category'].choices = [(c.id, c.name) for c in Category.objects.all()]
    #if request.method == 'POST' and form.is_valid():
        #name = form.cleaned_data['name']
        #description = form.cleaned_data['description']
        #cat = Category(
            #name=name,
            #description=description
        #)
        #cat.category_id = form.cleaned_data['category']
        #cat.save()
    #return render(request, 'category.html', {'form': form})


class CategoryAddView(View):
    def get(self, request):
        print("I am inside get function")
        form = CategoryForm()
        form.fields['category'].choices = [(c.id, c.name) for c in Category.objects.all()]        
        return render(request, 'category.html', {'form': form})
    
    def post(self, request):
        print("I am inside post function")
        form = CategoryForm(request.POST)
        form.fields['category'].choices = [(c.id, c.name) for c in Category.objects.all()]
        if form.is_valid():
            if self.save(form) is None:
                messages.add_message(request, messages.SUCCESS, 'Category Added successfully')
            else:
                messages.add_message(request, messages.SUCCESS, 'Some error occurred')
        
        return redirect('category')
    
    def save(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        cat = Category(
            name=name,
            description=description
        )
        cat.category_id = form.cleaned_data['category']
        return cat.save()        


class ProductAddView(FormView):
    template_name = 'productform.html'
    form_class = ProductForm
    success_url = '/products/add'
    
    def form_valid(self, form):
        # save to database
        print(form)
        return super().form_valid(form)
