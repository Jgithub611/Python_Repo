estudiantes=[]
option=0
#Función para agregar estudiantes
def add_estudiante():
    try:    
        nombre=input("Ingrese el nombre del estudiante: ")   
        edad=int(input("Ingrese la edad del estudiante: "))
        ID=int(input("Ingrese el ID del estudiante: "))
        if ID==find_estudiante(ID,True):
            print("***El estudiante ya está en sistema***")
        else:
            estudiante={"nombre":nombre,"ID":ID,"edad":edad}
            estudiantes.append(estudiante)
            print("***Estudiante asignado exitosamente***")
    except ValueError:
        print("El id y la edad deben ser valores enteros")
#Función para mostrar estudiantes
def show_estudiantes():
    if estudiantes==[]:
        print("No hay estudiantes registrados")
    else:
        print(estudiantes)
#Función para buscar estudiantes(utilizada de manera global, siendo llamada por otras funciones)
#El paramatro Function_call sirve para detectar si está siendo llamada desde el programa principal o desde una función.
def find_estudiante(ID,Function_call):
    index=-1
    if Function_call==True:
         for e in estudiantes:
            if e['ID']==ID:
                return ID
            else:
                return False
    else:
        ID=int(input("Ingrese el ID del estudiante: "))
        for e in estudiantes:
            index=index+1
            if e['ID']==ID:
                print(e)
                return index
            else:
                print("El estudiante no existe")
                return False
#Función para actualizar estudiantes               
def uptade_estudiantes():
    try:
        ID=find_estudiante(0,False)
        if ID==None:
            print("El estudiante no existe")
        else:
            nombre=input("Ingrese el nuevo nombre del estudiante: ")   
            edad=int(input("Ingrese la nueva edad del estudiante: "))
            ID1=int(input("Ingrese el nuevo ID del estudiante: "))
            estudiantes[ID]={"nombre":nombre,"ID":ID1,"edad":edad}
            print(f"El estudiante: {estudiantes[ID]} ha sido actualizado con éxito")
    except TypeError:
        print()
#Función para borrar estudiantes
def delete_estudiante():
    try:
        ID=find_estudiante(0,False)
        estudiantes.pop(ID)
        print(f"El estudiante ha sido eliminado con éxito")
    except TypeError:
        print("El estudiante no existe")

#Menú del usuario
while option !=6:
    try:
        option=int(input('''\nBienvenido al programa de gestión de estudiantes, escoga alguna de las siguientes opciones:
                        [1]Agregar un nuevo estudiante
                        [2]Mostrar lista de estudiantes
                        [3]Buscar un estudiante
                        [4]Actualizar información de un estudiante
                        [5]Eliminar a un estudiante
                        [6]Cerrar el programa
                        >'''))
        match option:
            case 1:
                add_estudiante()
            case 2:
                show_estudiantes()
            case 3:
                find_estudiante(0,False)
            case 4:
                uptade_estudiantes()
            case 5:
                delete_estudiante()
            case 6:
                exit()
            case _:
                print("Ingrese una opción valida")       
    except ValueError:
        print("Utilice un número entero")
