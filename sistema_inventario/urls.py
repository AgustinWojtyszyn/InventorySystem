from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    
    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    # Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/<int:id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/<int:id>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
