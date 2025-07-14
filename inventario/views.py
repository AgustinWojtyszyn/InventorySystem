from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Producto, Proveedor, HistorialStock
from .forms import ProductoForm, ProveedorForm
from django.db.models import Q

@login_required
def home(request):
    productos_count = Producto.objects.count()
    proveedores_count = Proveedor.objects.count()
    return render(request, 'inventario/home.html', {
        'productos_count': productos_count,
        'proveedores_count': proveedores_count,
    })

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_productos')
    else:
        form = UserCreationForm()
    return render(request, 'inventario/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_productos')
    else:
        form = AuthenticationForm()
    return render(request, 'inventario/login.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def lista_productos(request):
    query = request.GET.get('q')
    productos = Producto.objects.all()
    
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(proveedor__nombre__icontains=query)
        )
    
    return render(request, 'inventario/lista_productos.html', {
        'productos': productos,
        'query': query
    })

@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    historial = HistorialStock.objects.filter(producto=producto).order_by('-fecha')[:10]
    return render(request, 'inventario/detalle_producto.html', {
        'producto': producto,
        'historial': historial
    })

@login_required
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            
            # Registrar en el historial
            HistorialStock.objects.create(
                producto=producto,
                usuario=request.user,
                cantidad_anterior=0,
                cantidad_nueva=producto.cantidad
            )
            
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/form_producto.html', {'form': form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    cantidad_anterior = producto.cantidad
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            
            # Registrar en el historial solo si cambió la cantidad
            if cantidad_anterior != producto.cantidad:
                HistorialStock.objects.create(
                    producto=producto,
                    usuario=request.user,
                    cantidad_anterior=cantidad_anterior,
                    cantidad_nueva=producto.cantidad
                )
            
            return redirect('detalle_producto', id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/form_producto.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/confirmar_eliminar.html', {'producto': producto})

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/lista_proveedores.html', {'proveedores': proveedores})

@login_required
def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventario/form_proveedor.html', {'form': form})

@login_required
def detalle_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'inventario/detalle_proveedor.html', {'proveedor': proveedor})

@login_required
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('detalle_proveedor', id=proveedor.id)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventario/form_proveedor.html', {'form': form})

@login_required
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'inventario/confirmar_eliminar_proveedor.html', {'proveedor': proveedor})
