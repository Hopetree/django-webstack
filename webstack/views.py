from django.shortcuts import render
from .models import FirstMenu


# Create your views here.

def index(request):
    first_menus = FirstMenu.objects.order_by('sort_order')
    return render(request, context={'first_menus': first_menus},
                  template_name='webstack/index.html')
