from django.shortcuts import render, redirect
from .forms import NewUserForm

# Create your views here.
def register(request):
    form = NewUserForm()
    context = {
        'form' : form,
    }
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/myapp/products')
    return render(request, 'users/register.html', context)
