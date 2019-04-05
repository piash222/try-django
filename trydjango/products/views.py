from django.shortcuts import render
from .form import ProductForm

# Create your views here.
def form_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    
    return render(request, 'products/form_create.html', context)


def form_create_raw(request):
    print(type(request.GET))
    print(type(request.POST))
    return render(request, 'products/form_create_raw.html', {})
