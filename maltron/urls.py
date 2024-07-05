from django.urls import path
from .views import index, lista_productos, login_view, registro, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, ver_carrito
from django.contrib.auth.views import LogoutView

from maltron import views

urlpatterns = [
    path('', index, name='index'),
    path('productos/', lista_productos, name='lista_productos'),
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('agregar/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', restar_producto, name='restar_producto'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
    path('carrito/', ver_carrito, name='carrito'),
    
]