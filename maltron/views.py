from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Producto
from .Carrito import Carrito
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import ContactoForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Error en el login")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# views.py en la carpeta maltron

def index(request):
    productos = Producto.objects.all()
    return render(request, 'maltron/index.html', {'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()  # Suponiendo que Producto es tu modelo
    context = {
        'Productos': productos
    }
    return render(request, 'maltron/base.html', context)

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not User.objects.filter(username=nombre).exists():
            user = User.objects.create_user(nombre, email, password)
            user.save()
            messages.success(request, "Usuario creado correctamente")
            return redirect('login')
        else:
            messages.error(request, "El nombre de usuario ya existe")
    return render(request, 'registration/registro.html')
    
def base(request):
    productos = Producto.objects.all()
    return render(request, 'maltron/base.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)  
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('carrito')

def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def ver_carrito(request):
    carrito = Carrito(request)
    context = {'carrito': carrito}
    return render(request, 'maltron/carrito.html', context)



