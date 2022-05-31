import os

CARPETA = 'clientes/'
EXTENSION = '.txt'

#CLIENTES
class Cliente:
    def __init__(self, nombre_completo, direccion, ciudad, telefono, email, fecha_nacimiento, autos, notas):
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.autos = autos
        self.notas = notas

def app():
    crear_directorio()
    mostrar_menu()
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_cliente()
            preguntar: False
        elif opcion == 2:
            editar_cliente()
            preguntar: False
        elif opcion == 3:
            buscar_cliente()
            preguntar: False
        elif opcion == 4:
            mostrar_clientes()
            preguntar: False
        elif opcion == 5:
            eliminar_cliente()
            preguntar: False
        else:
            print('Opción no válida, intente de nuevo')

def mostrar_menu():
    print('Seleccione una operación del menú:')
    print('1) Agregar nuevo cliente')
    print('2) Editar cliente')
    print('3) Buscar cliente')
    print('4) Ver clientes')
    print('5) Eliminar cliente')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def agregar_cliente():
    print('Escribe los datos para agregar el nuevo cliente')
    nombre_cliente = input('Nombre completo del cliente: \r\n')
    existe = existe_cliente(nombre_cliente)
    if not existe:
        with open(CARPETA + nombre_cliente + EXTENSION, 'w', encoding="utf8") as archivo:
            direccion_cliente = input('Agrega la dirección: \r\n')
            ciudad_cliente = input('Agrega la Ciudad: \r\n')
            telefono_cliente = input('Agrega el teléfono: \r\n')
            email_cliente = input('Agrega el email: \r\n')
            fecha_nacimiento_cliente = input('Agrega la fecha de nacimiento: \r\n')
            autos_cliente = input('Agrega los autos: \r\n')
            notas_cliente = input('Agrega las notas: \r\n')
            # Instanciar la clase
            cliente = Cliente(nombre_cliente, direccion_cliente, ciudad_cliente, telefono_cliente, email_cliente, fecha_nacimiento_cliente, autos_cliente, notas_cliente)
            archivo.write('Nombre completo: ' + cliente.nombre_completo + '\r\n')
            archivo.write('Dirección: ' + cliente.direccion + '\r\n')
            archivo.write('Ciudad: ' + cliente.ciudad + '\r\n')
            archivo.write('Teléfono: ' + cliente.telefono + '\r\n')
            archivo.write('Email: ' + cliente.email + '\r\n')
            archivo.write('Fecha de nacimiento: ' + cliente.fecha_nacimiento + '\r\n')
            archivo.write('Autos: ' + cliente.autos + '\r\n')
            archivo.write('Notas: ' + cliente.notas + '\r\n')
            print('\r\n Cliente creado exitosamente \r\n')
    else:
      print('Ese cliente ya existe')
    app()

def editar_cliente():
    print('Escribe el nombre del cliente a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = existe_cliente(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w', encoding="utf8") as archivo:
            nombre_cliente = input('Agrega el nuevo nombre: \r\n')
            direccion_cliente = input('Agrega la dirección: \r\n')
            ciudad_cliente = input('Agrega la Ciudad: \r\n')
            telefono_cliente = input('Agrega el teléfono: \r\n')
            email_cliente = input('Agrega el email: \r\n')
            fecha_nacimiento_cliente = input('Agrega la fecha de nacimiento: \r\n')
            autos_cliente = input('Agrega los autos: \r\n')
            #Instanciar
            cliente = Cliente(nombre_cliente, direccion_cliente, ciudad_cliente, telefono_cliente, email_cliente, fecha_nacimiento_cliente, autos_cliente)
            archivo.write('Nombre completo: ' + cliente.nombre_completo + '\r\n')
            archivo.write('Dirección: ' + cliente.direccion + '\r\n')
            archivo.write('Ciudad: ' + cliente.ciudad + '\r\n')
            archivo.write('Teléfono: ' + cliente.telefono + '\r\n')
            archivo.write('Email: ' + cliente.email + '\r\n')
            archivo.write('Fecha de nacimiento: ' + cliente.fecha_nacimiento + '\r\n')
            archivo.write('Autos: ' + cliente.autos + '\r\n')
            archivo.write('Notas: ' + cliente.notas + '\r\n')
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_cliente + EXTENSION)
        print('\r\n Cliente editado exitosamente \r\n')
    else:
        print('Ese cliente no existe')
        app()

def buscar_cliente():
    print('Escribe el nombre del cliente que deseas buscar')
    nombre_cliente = input('Nombre del cliente que desea buscar: \r\n')
    existe = existe_cliente(nombre_cliente)
    if existe:
        with open(CARPETA + nombre_cliente + EXTENSION, 'r', encoding="utf8") as archivo:
            print('\r\n Información del Cliente: \r\n')
            for linea in archivo:
                print(linea.rstrip())
            print('Cliente encontrado exitosamente!! \r\n')
    else:
        print(' \r\n El cliente que usted busca no existe no existe \r\n')
    app()

def mostrar_clientes():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        #print('Nombre: ' + archivo)
        with open(CARPETA + archivo, 'r', encoding="utf8") as cliente:
            for linea in cliente:
                print(linea.rstrip())
            print('\r\n')
    app()

def eliminar_cliente():
    nombre_completo = input('Seleccione el contacto que desea eliminar: \r\n')
    existe = existe_cliente(nombre_completo)
    if existe:
        os.remove(CARPETA + nombre_completo + EXTENSION)
        print('\r\n Contacto eliminado correctamente \r\n')
    else:
        print('\r\n No existe el contacto que desea eliminar \r\n')
    app()

def existe_cliente(nombre_completo):
    return os.path.isfile(CARPETA + nombre_completo + EXTENSION)
app()

