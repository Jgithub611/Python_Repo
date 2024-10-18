
import time

Usser={
    "Usser01":{"ID":11,"password":123,"Blocked":False,"name":"Ussername","cuenta":"Corriente","saldo":1000.0},
    "Usser02":{"ID":12,"password":456,"Blocked":False,"name":"Ussername1","cuenta":"Ahorros","saldo":12.0},
    "Usser03":{"ID":13,"password":789,"Blocked":False,"name":"Ussername2","cuenta":"Corriente","saldo":9500.0}}

estado_cuenta=lambda usser: print(f"En su cuenta de tipo {usser["cuenta"]} su saldo actual es de: {usser["saldo"]}")#Función lambda para mostrar el estado de cuenta

def deposito(usser): #función para depositar a la cuenta según su ID
    try:
        monto=float(input("Ingrese la cantidad a depositar: "))
        usser["saldo"]+=monto
        print(f"Operación realizada con éxitro (saldo actual: {usser["saldo"]})")
    except ValueError: print("Utilice una cifra númerica para el monto a depositar") #Error de entrada de datos

def retiro(usser):#función para retirar en la cuenta según su ID
    try:
        monto=float(input("Ingrese la cantidad a retirar: "))
        if usser["saldo"]<monto: #El usuario no puede retirar más fondos de los que tiene en su cuenta actualmente
            print(f"Fondos insuficientes (saldo actual: {usser["saldo"]})")
        else:
            usser["saldo"]-=monto
            print(f"Operación realizada con éxito (saldo actual: {usser["saldo"]})")#Salida para operación exitosa
    except ValueError: print("Utilice una cifra númerica para el monto a depositar")#Error de entrada de datos

def admin_mode(): #Función que simula el acceso de un admonistrador para verificar la cantidad de usuarios y sus datos
    passw=int(input("Ingrese la contraseña de administrador:"))
    if passw==137611: print(UsserList[:]) 
    else: print("Acesso de administrador denegado"), exit()

def usser_valid():#Función para validar que el usuario exista y verificar que usuario es según su ID
    valid,access=False,False
    sleep,intentos=5,5
    while True:  
        try:
            ID=int(input("Ingrese su ID: "))
            if ID==611:
                admin_mode()
              
            for e in Usser:
             if ID==Usser[e]["ID"]:
                S_User=Usser[e]
                valid=True
                break
        except ValueError: print("Utilice un número entero")#Error de entrada de datos
        if valid==True:
            while intentos>0:
                if intentos<=3:#Si el usuario ingresa una contraseña incorrecta más de N veces, comenzará el contador como penalización
                    for i in range(sleep, 0, -1):
                        print(f"Demasiados intentos fallidos, espere {i} segundos para volver a intentarlo...", end="\r")
                        time.sleep(1)
                    sleep+=5#El tiempo de penalización aumenta con el número de intentos
                try:    
                    u_password=int(input("\nIngrese su contraseña: "))
                except  ValueError: print("Ingrese un número entero")#Error de entrada de datos
                if S_User["password"]==u_password:#Verificación de la contraseña
                    access=True
                    print(f"¡Bienvenido {S_User["name"]}!")
                    break
                else:
                    print("Contraseña invalida")
                    intentos-=1
            if access==True:            
                while True:
                    try:
                        option=int(input('''Selecione la operación a realizar:
                                        [1]Estado de cuenta
                                        [2]Deposito
                                        [3]Retiro
                                        [4]Salir
                                        >'''))
                        match option:
                            case 1: estado_cuenta(S_User)
                            case 2: deposito(S_User)
                            case 3: retiro(S_User)
                            case 4: exit()
                            case _: print("Ingrese una opción valida")       
                    except ValueError: print("Utilice un número entero")#Error de entrada de datos
            else:
                print("Acesso denegado, clave bloqueada")
                exit() 
        else: print("Usuario no registrado")    
usser_valid()