from django.shortcuts import render
from django.http import HttpResponse
# from collections import namedtuple

from .models import Category


# Create your views here.
def get_categories_old(request):
    # def get_body(arg):
    #     return 'Hello Categories'
    # Response = namedtuple('Response',
    #   ['get', 'status_code', '_closable_objects'])
    # return Response(
    #   get=get_body,
    #   status_code=200,
    #   _closable_objects=False
    # )
    html = "<html><head></head><body><ul>"
    items = Category.objects.all()
    for item in items:
        html += '<li>' + item.name + '</li>'
    html += "</ul></body></html>"
    return HttpResponse(html)


def get_categories(request):
    items = Category.objects.all()
    return render(
      request,
      'get_categories.html',
      {'items': items}
   )
