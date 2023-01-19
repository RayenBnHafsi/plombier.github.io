from django.shortcuts import render
from .models import Slider

# Create your views here.
def index(request):
    slides = Slider.objects.order_by('order')
    return render(
        request, 'base.html', 
        {
            'slides': slides
        }
    )

def product(request,):
    return render(
        request, 'product.html'
    )


def slider(request,):
    return render(
        request, 'slider.html'
    )