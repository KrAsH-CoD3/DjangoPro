from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products

# Create your views here.
def index(request):
    return HttpResponse("Hi, This is this index page. This is gonna be great!<br/> Click here to go <a href='products'>Product<a/>")

def products(request):
    products = Products.objects.all()
    context =  {
        'id': id,   
        'products': products
    }
    return render(request, 'myapp/index.html', context)

def product_detail(request, id):
    product = Products.objects.get(id=id)
    context =  {
        'id': id,
        'product': product,
    }
    return render(request, 'myapp/product_detail.html', context)

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        product = Products(name=name, price=price, desc=desc, image=image)
        product.save()
    return render(request, 'myapp/addproduct.html')

def update_product(request, id):
    product = Products.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    context = {
        "product": product
    }
    return render(request, 'myapp/updateproduct.html', context)

def delete_product(request, id):
    product = Products.objects.get(id=id)
    context = {
        "product" : product,
    }
    if request.method == "POST":
        product.delete()
        return redirect('/myapp/products')
    return render(request, 'myapp/delete.html', context)