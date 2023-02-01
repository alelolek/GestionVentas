import os
from tabulate import tabulate
import requests

def iniciar():
    os.system('clear')
    while True:
        print('Elige una opcion: ')
        print('1. Registrar producto')
        print('2. Consultar  todos los productos')
        print('3. Buscar producto')
        print('4. modificar producto')
        print('5. Eliminar producto')
        print('6. Realizar venta')
        print('7. Salir')
        opcion = input('Ingresa una opcion: ')

        if opcion == '1':
            nuevoProducto()
        elif opcion =='2':
            verProductos()
        elif opcion =='3':
            buscarProducto()
        elif opcion =='4':
            modificarProducto()
        elif opcion == '5':
            eliminarProducto()
        elif opcion == '6':
            nuevaVenta()
        elif opcion == '7':
            break

def nuevoProducto():
    nombre = input('Ingresa el nombre: ')
    descripcion = input('Ingresa la descripcion: ')
    precio = input('Ingresa el precio: ')
    data = {'nombre': nombre, 'descripcion': descripcion,'precio':precio}
    respuesta = requests.post(url='http://localhost:3000/productos/registrar',data=data)
    print(respuesta.text)



def verProductos():
    respuesta = requests.get(url='http://localhost:3000/productos/todos')
    datos = []
    for dato in respuesta.json():
        temp = []
        for key , value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID','NOMBRE','DESCRIPCION','PRECIO']
    tabla  = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)


def buscarProducto():
    id = input('Ingrese el id del producto a buscar: ')
    respuesta = requests.get(url='http://localhost:3000/productos/buscar/'+id)
    datos = []
    for dato in respuesta.json():
        temp = []
        for key , value in dato.items():
            temp.append(value)
        datos.append(temp)
    headers = ['ID','NOMBRE','DESCRIPCION','PRECIO']
    tabla  = tabulate(datos,headers,tablefmt='fancy_grid')
    print(tabla)


def modificarProducto():
    id = input('Ingrese el id del producto a modificar: ')
    campo = input('Selecciona el campo a modificar: \n1. Nombre\n2. Descripcion\n3. Precio')
    nuevo_valor = input('Ingrese el nuevo valor: ')
    data = {'campo': campo,'nuevo_valor': nuevo_valor}
    respuesta = requests.post(url='http://localhost:3000/productos/modificar/'+id,data=data)
    print(respuesta.text)
    

def eliminarProducto():
    id = input('Ingrese el id del producto a eliminar: ')
    respuesta = requests.post(url='http://localhost:3000/productos/eliminar/'+id)
    print(respuesta.text)


def nuevaVenta():
    cliente = input('Ingresa el nombre del cliente: ')
    total = 0
    productos = []
    print('Seleccione los productos. Presione 0 para salir.')
    while True:
        id = input('Ingrese el id del producto: ')
        if(id=='0'):
            break
        else:
            producto = requests.get(url='http://localhost:3000/productos/buscar/'+id)
            if len (producto.json()):
                nombre = producto.json()[0]['nombre']
                precio = producto.json()[0]['precio']
                cantidad = input('Ingrese la cantidad: ')
                totalPorProducto = int(cantidad)* float(precio)
                total += totalPorProducto
                productos.append([id,nombre,precio,cantidad,totalPorProducto])
                mostrarVenta(cliente,productos,total)
            else:   
                print('Producto no encontrado!!')


def mostrarVenta(cliente,productos,total):
    print('\n\t\tComprobante de Venta')
    print('\nCliente: '+cliente)
    headers = ['ID','NOMBRE','PRECIO','CANTIDAD','TOTAL']
    tabla  = tabulate(productos,headers,tablefmt='simple')
    print(tabla)
    print('\t\t\tTotal a pagar '+ str(total))




iniciar()