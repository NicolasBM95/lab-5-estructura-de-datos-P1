#Clase fecha
class fecha:
    #Función constructora de los atributos
    def __init__(self, dd, mm, aa):
        self.dd = dd
        self.mm = mm
        self.aa = aa
    #Funciónes set
    def setDia(self, dia):
        self.dd = dia
    def setMes(self, mes):
        self.mm = mes
    def setA(self, year):
        self.aa = year
    #Funciónes get
    def getDia(self):
        return self.dd
    def getMes(self):
        return self.mm
    def getA(self):
        return self.aa
    #Función __str__ para definir que aparecerá en consola al hacer un print(fecha)
    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.aa}"

class direccion:
#Función constructora de los atributos 
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto
    #Funciónes set
    def setCalle(self, calle):
        self.calle = calle
    def setNomenclatura(self, nomenclatura):
        self.nomenclatura = nomenclatura
    def setBarrio(self, barrio):
        self.barrio = barrio
    def setCiudad(self, ciudad):
        self.ciudad = ciudad
    def setEdificio(self, edificio):
        self.edificio = edificio
    def setApto(self, apto):
        self.apto = apto
    #Funciónes get
    def getCalle(self):
        return self.calle
    def getNomenclatura(self):
        return self.nomenclatura
    def getBarrio(self):
        return self.barrio
    def getCiudad(self):
        return self.ciudad
    def getEdificio(self):
        return self.edificio
    def getApto(self):
        return self.apto
    def __str__(self):
        return f"Calle: {self.calle}, Nomenclatura: {self.nomenclatura}, Barrio: {self.barrio}, Ciudad: {self.ciudad}, Edificio: {self.edificio}, Apto: {self.apto}"

#Clase usuario
class usuario:
    #función constructora de los atributos
    def __init__(self, nombre, cedula, id, contraseña, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.nombre = nombre
        self.cedula = cedula
        self.id = id
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha(dd, mm, aa)
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
    #Funciones set
    def setNombre(self, nombre):
        self.nombre = nombre
    def setCedula(self, cedula):
        self.cedula = cedula
    def setId(self, id):
        self.id = id
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    def setFecha_Nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def setCiudad_Nacimiento(self, ciudad_nacimiento):
        self.ciudad_nacimiento = ciudad_nacimiento
    def setTel(self, tel):
        self.tel = tel
    def setEmail(self, email):
        self.email = email
    def setDir(self, dir):
        self.dir = dir
    #Funciones Get
    def getNombre(self):
        return self.nombre
    def getCedula(self):
        return self.cedula
    def getId(self):
        return self.id
    def getContraseña(self):
        return self.contraseña
    def getFecha_Nacimiento(self):
        return self.fecha_nacimiento
    def getCiudad_Nacimiento(self):
        return self.ciudad_nacimiento
    def getTel(self):
        return self.tel
    def getEmail(self):
        return str(self.email)
    def getDir(self):
        return self.dir
    #Función __str__
    def __str__(self):
        return f"Nombre: {self.nombre}, Cedula: {self.cedula} ID: {self.id}, Fecha de Nacimiento: {self.fecha_nacimiento}, Ciudad de Nacimiento: {self.ciudad_nacimiento}, Teléfono: {self.tel}, Email: {self.email}, Dirección: {self.dir}"

# Clase administrador que hereda de usuario
class administrador(usuario):
    def __init__(self, nombre, cedula, id, contraseña, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto):
        super().__init__(nombre, cedula, id, contraseña, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto)



#Clase nodo doble que trae los usuario/empleado
class NodoDoble:
    def __init__(self, usuario):
        self.usuario = usuario
        self.next = None
        self.prev = None
    #Funciones set
    def setUsuario(self,nuevo_usuario):
        self.usuario = nuevo_usuario
    def setNext(self, nuevo_nodo):
        self.next = nuevo_nodo
    def setPrev(self, nuevo_nodoprevio):
        self.prev = nuevo_nodoprevio
    #Funciones get
    def getUsuario(self):
        return self.usuario
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    #Funcion __str__
    def __str__(self):
        return str(self.usuario)

#Clase lista doble de empleados
class empleados:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #Funciones
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def addfirst(self, usuario):
        nuevo_nodo = NodoDoble(usuario)
        if empleados.isEmpty(self):
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nuevo_nodo.setNext(self.head)
            self.head.setPrev(nuevo_nodo)
            self.head = nuevo_nodo
            self.ordenamiento_ID()
        self.size += 1
    def addlast(self, usuario):
        nuevo_nodo = NodoDoble(usuario)
        if empleados.isEmpty(self):
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.setNext(nuevo_nodo)
            nuevo_nodo.setPrev(self.tail)
            self.tail = nuevo_nodo
            self.ordenamiento_ID()
        self.size += 1
    def removefirst(self):
        if empleados.isEmpty(self):
            return None
        else:
            nodo_temporal = self.head
            self.head = nodo_temporal.getNext()
            nodo_temporal.setNext(None)
            nodo_temporal.setPrev(None)
            self.size -= 1
            return nodo_temporal.getUsuario()
    def removelast(self):
        if empleados.isEmpty(self):
            return None
        else:
            nodo_temporal = self.tail
            self.tail = nodo_temporal.getprev()
            nodo_temporal.setNext(None)
            nodo_temporal.setPrev(None)
            self.size -= 1
            return nodo_temporal.getUsuario()
    def remove(self, nodo_para_eliminar):
        if nodo_para_eliminar == self.head:
            return empleados.removefirst
        elif nodo_para_eliminar == self.tail:
            return empleados.removelast
        else:
            usuario_para_eliminar = nodo_para_eliminar.getUsuario()
            nodo_temporal_prev = nodo_para_eliminar.getPrev()
            nodo_temporal_next = nodo_para_eliminar.getNext()
            nodo_temporal_prev.setNext(nodo_temporal_next)
            nodo_temporal_next.setPrev(nodo_temporal_prev)
            usuario_para_eliminar.setNext(None)
            usuario_para_eliminar.setPrev(None)
            self.size -= 1
            return usuario_para_eliminar
    def addbefore(self, nodo_existente, usuario):
        if nodo_existente == self.head:
            empleados.addfirst(usuario)
        else:
            nuevo_nodo = NodoDoble(usuario)
            nodo_temporal_prev = nodo_existente.getPrev()
            nodo_temporal_prev.setNext(nuevo_nodo)
            nuevo_nodo.setPrev(nodo_temporal_prev)
            nuevo_nodo.setNext(nodo_existente)
            nodo_existente.setPrev(nuevo_nodo)
            self.size += 1
        self.ordenamiento_ID()
    def addafter(self, nodo_existente, usuario):
        if nodo_existente == self.tail:
            empleados.addlast(usuario)
        else:
            nuevo_nodo = NodoDoble(usuario)
            nodo_temporal_next = nodo_existente.getNext()
            nodo_existente.setNext(nuevo_nodo)
            nuevo_nodo.setPrev(nodo_existente)
            nuevo_nodo.setNext(nodo_temporal_next)
            nodo_temporal_next.setPrev(nuevo_nodo)
            self.size += 1
        self.ordenamiento_ID()
    # Algoritmo de ordenamiento por ID con Ordenamiento por inserción
    def ordenamiento_ID(self):
        if self.head is None:
            return
        nodo_temporal = self.head.getNext()
        while nodo_temporal is not None:
            usuario_temporal = nodo_temporal.getUsuario()
            j = nodo_temporal
            while j.getPrev() is not None and j.getPrev().getUsuario().getId() > usuario_temporal.getId():
                j.setUsuario(j.getPrev().getUsuario())
                j = j.getPrev()
            j.setUsuario(usuario_temporal)
            nodo_temporal = nodo_temporal.getNext()
    def guardar_en_archivo(self, nombre_archivo="empleados.txt"):
        self.ordenamiento_ID()
        nodo_usuario_temp = self.head
        with open(nombre_archivo, "w") as archivo:
            while nodo_usuario_temp is not None:
                archivo.write(str(nodo_usuario_temp) + "\n")
                nodo_usuario_temp = nodo_usuario_temp.next
    def mostrar_archivo(self, nombre_archivo="empleados.txt"):
        with open(nombre_archivo, "r") as archivo:
            print(archivo.read())
    def guardar_en_archivo(self, nombre_archivo="Password.txt"):
            self.ordenamiento_ID()
            nodo_usuario_temp = self.head
            with open(nombre_archivo, "w") as archivo:
                while nodo_usuario_temp is not None:
                    archivo.write(f"{nodo_usuario_temp.usuario.cedula},{nodo_usuario_temp.usuario.contraseña},{type(nodo_usuario_temp.usuario).__name__}\n")
                    nodo_usuario_temp = nodo_usuario_temp.next
    def mostrar_archivo(self, nombre_archivo="Password.txt"):
        with open(nombre_archivo, "r") as archivo:
            print(archivo.read()) 
    def iniciar_sesion(lista_empleados):
        cedula = input("Ingrese su número de cédula: ")
        contraseña = input("Ingrese su contraseña: ")

        with open("Password.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == cedula and datos[1] == contraseña:
                    if datos[2] == "administrador":
                        print(f"Bienvenido administrador {cedula}")
                        empleados.menu_administrador(lista_empleados)
                    elif datos[2] == "usuario":
                        print(f"Bienvenido empleado {cedula}")
                        empleados.menu_empleado()
                    return
        print("Credenciales incorrectas. Intente de nuevo.")
    def menu_empleado():
        print("Menú de Empleado")
        print("1. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Sesión cerrada.")
    def menu_administrador(lista_empleados):
        while True:
            print("Menú de Administrador")
            print("1. Crear usuario")
            print("2. Eliminar usuario")
            print("3. Editar contraseña de usuario")
            print("4. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                empleados.crear_usuario(lista_empleados)
            elif opcion == "2":
                empleados.eliminar_usuario(lista_empleados)
            elif opcion == "3":
                empleados.editar_contraseña(lista_empleados)
            elif opcion == "4":
                print("Sesión cerrada.")
                break
    def crear_usuario(lista_empleados):
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        id = input("ID: ")
        contraseña = input("Contraseña: ")
        dd = int(input("Día de nacimiento: "))
        mm = int(input("Mes de nacimiento: "))
        aa = int(input("Año de nacimiento: "))
        ciudad_nacimiento = input("Ciudad de nacimiento: ")
        tel = input("Teléfono: ")
        email = input("Email: ")
        calle = input("Calle: ")
        nomenclatura = input("Nomenclatura: ")
        barrio = input("Barrio: ")
        ciudad = input("Ciudad: ")
        edificio = input("Edificio: ")
        apto = input("Apartamento: ")

        tipo_usuario = input("¿Es administrador? (s/n): ").lower()
        if tipo_usuario == "s":
            nuevo_usuario = administrador(nombre, cedula, id, contraseña, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto)
        else:
            nuevo_usuario = usuario(nombre, cedula, id, contraseña, dd, mm, aa, ciudad_nacimiento, tel, email, calle, nomenclatura, barrio, ciudad, edificio, apto)

        lista_empleados.addlast(nuevo_usuario)
        lista_empleados.guardar_en_archivo()
    def eliminar_usuario(lista_empleados):
        cedula = input("Ingrese la cédula del usuario a eliminar: ")
        nodo_actual = lista_empleados.head
        while nodo_actual is not None:
            usuario_actual = nodo_actual.getUsuario()
            if usuario_actual.getCedula() == cedula:
                lista_empleados.remove(nodo_actual)
                print(f"Usuario con cédula {cedula} eliminado correctamente.")
                return
            nodo_actual = nodo_actual.getNext()
        
        print("Usuario no encontrado.")
    def editar_contraseña(lista_empleados):
        cedula = input("Ingrese la cédula del usuario a editar: ")
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        nodo_actual = lista_empleados.head
        while nodo_actual is not None:
            if nodo_actual.getUsuario().getCedula() == cedula:
                nodo_actual.getUsuario().setContraseña(nueva_contraseña)
                lista_empleados.guardar_en_archivo()
                print("Contraseña actualizada.")
                return
            nodo_actual = nodo_actual.getNext()
        print("Usuario no encontrado.")

# Ejemplo de uso

# Crear instancias de usuario y administrador
admin = administrador("Admin", "00000000", "1", "adminpass", 10, 10, 1980, "Bogotá", "111111111", "admin@example.com", "Calle Admin", "A1", "Centro", "Bogotá", "Edificio Admin", "1")
empleado = usuario("Empleado", "11111111", "2", "emppass", 5, 5, 1990, "Bogotá", "222222222", "empleado@example.com", "Calle Emp", "E1", "Centro", "Bogotá", "Edificio Emp", "2")

# Crear la lista doblemente enlazada
listaEmpleados = empleados()

# Insertar usuarios
listaEmpleados.addfirst(admin)
listaEmpleados.addlast(empleado)

# Guardar los usuarios en el archivo
listaEmpleados.guardar_en_archivo()

# Iniciar sesión
empleados.iniciar_sesion(listaEmpleados)