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
