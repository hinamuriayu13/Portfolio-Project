from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegisterForm
from .models import Product
from .cart import Cart


# Create your views here.
def index(request):
    return render(request, 'index.html')

def product_page(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_page.html', {'product': product})




#Register view 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login_view')
    else:
        form = UserRegisterForm()
    return render(request, 'login.html', {'form': form, 'register': True})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")
    else:
        form = AuthenticationForm() 
    return render(request, "login.html", {"form": form})

@login_required
def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login_view') 


#cart views

def cart_summary(request):
    return render(request, 'cart_summary.html',{})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'Product Description': product.description})
        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass