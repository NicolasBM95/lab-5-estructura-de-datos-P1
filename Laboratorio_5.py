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
        actual = self.head
        with open(nombre_archivo, "w") as archivo:
            while actual is not None:
                archivo.write(str(actual) + "\n")
                actual = actual.next
    def mostrar_archivo(self, nombre_archivo="empleados.txt"):
        with open(nombre_archivo, "r") as archivo:
            print(archivo.read())

# Crear instancias de usuario
usuario1 = usuario("Juan Perez", "12345678", "5", 1, 1, 1990, "Bogotá", "123456789", "juan.perez@example.com", "Calle 123", "A123", "Centro", "Bogotá", "Edificio X", "101")
usuario2 = usuario("Ana Gomez", "87654321", "7", 2, 2, 1992, "Medellín", "987654321", "ana.gomez@example.com", "Calle 456", "B456", "Norte", "Medellín", "Edificio Y", "202")
usuario3 = usuario("Carlos Diaz", "11223344", "2", 3, 3, 1985, "Cali", "112233445", "carlos.diaz@example.com", "Calle 789", "C789", "Sur", "Cali", "Edificio Z", "303")

# Crear la lista doblemente enlazada
listaEmpleados = empleados()

# Insertar usuarios
listaEmpleados.addfirst(usuario1)
listaEmpleados.addlast(usuario2)
listaEmpleados.addafter(listaEmpleados.head, usuario3)

# Guardar los usuarios en el archivo
listaEmpleados.guardar_en_archivo()

# Mostrar el contenido del archivo
listaEmpleados.mostrar_archivo()