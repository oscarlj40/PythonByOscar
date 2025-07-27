import random
import os

# creacion de clase persona, que será utilizada para poder asignar nombre
# y apellido a un cliente
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# clase cliente, que será utilizada para identificar a las personas
# que interactuen con la app de banco
class Cliente(Persona):
    lstClientes = []

    def __init__(self, nombre, apellido, numero_cuenta, balance ):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # funcion para imprimir un desglose de la información del cliente
    def imprimir(self):
        os.system("cls")
        print("\nEstos son los datos del cliente: ")
        print(f"NOMBRE: {self.nombre}")
        print(f"APELLIDO: {self.apellido}")
        print(f"NUMERO DE CUENTA: {self.numero_cuenta}")
        print(f"BALANCE: ${self.balance}")
        input("\nPRESS ENTER...")
        os.system("cls")

    # funcion para realizar depositos a la cuenta del cliente
    def depositar(self):
        os.system("cls")
        try:
            dinero = float(input("\nCUANTO DINERO VAS A DEPOSITAR? : "))
            if dinero > 0:
                self.balance += dinero
                print(f"\nSE GUARDO EL DINERO CON EXITO, NUEVO BALANCE ${self.balance}\n")
                input("\nPRESS ENTER...")
                os.system("cls")
            else:
                print("\nNO PUEDES DEPOSITAR CANTIDADES NEGATIVAS O CERO\n")

        except ValueError:
            print("\nERROR: INGRESA UN NUMERO VALIDO BOBO\n")
            input("\nPRESS ENTER...")
            os.system("cls")

    # funcion para realizar un retiro de dinero de la cuenta del cliente
    def retirar(self):
        os.system("cls")
        try:
            dinero_retirar = float(input("\nCUANTO DINERO VAS A RETIRAR? : "))
            if dinero_retirar > 0:
                if dinero_retirar > self.balance:
                    print("\nFONDOS INSUFICIENTES\n")
                else:
                    self.balance -= dinero_retirar
                    print(f"\nDINERO RETIRADO CON EXITO, NUEVO BALANCE ${self.balance}\n")
                input("\nPRESS ENTER...")
                os.system("cls")
            else:
                print("\nNO PUEDES RETIRAR CANTIDADES NEGATIVAS O CERO\n")

        except ValueError:
            print("\nERROR: INGRESA UN NUMERO VALIDO BOBO\n")
            input("\nPRESS ENTER...")
            os.system("cls")

# funcion para crear un cliente nuevo en la app de banco
def crear_cliente():

    os.system("cls")
    print("\nHOLA, INGRESA LOS SIGUIENTE DATOS:\n")
    nombre = input("NOMBRE: ").upper()
    apellido = input("APELLIDO: ").upper()

    cuenta_bancaria = "".join(str(random.randint(0, 9)) for _ in range(10))

    balance = 0

    cliente_creado = Cliente(nombre, apellido, cuenta_bancaria, balance)
    cliente_creado.lstClientes.append(cliente_creado)

    print("\nCUENTA CREADA CON EXITO...\n")

    Cliente.imprimir(cliente_creado)

# funcion para mostrar el menu de inicio de la app de banco
def inicio():

    os.system("cls")
    print(f"\nBIENVENIDO A LA APP BANCARIA {cliente_a.nombre} {cliente_a.apellido} :D\n")
    print("EN QUE TE PUEDO AYUDAR")
    resp2 = input("1) DEPOSITAR \n2) RETIRAR \n3) INFORMACION DE CLIENTE \n4) CERRAS SESION \n -----> ")

    match resp2:
        case '1':
            cliente_a.depositar()
            inicio()

        case '2':
            cliente_a.retirar()
            inicio()

        case '3':
            cliente_a.imprimir()
            inicio()

        case '4':
            print(f"\nHASTA LUEGO {cliente_a.nombre} {cliente_a.apellido} :D")
            input("\nPRESS ENTER...")
            os.system("cls")
            return

        case _:
            print("\nEL CARACTER QUE INGRESASTE ES INCORRECTO D:\n")
            input("\nPRESS ENTER...")
            os.system("cls")


i = 0
while i == 0:
    os.system("cls")
    print("\nBIENVENIDO A LA APP BANCARIA :D\n")
    resp1 = input("1) INICIAR SESION \n2) CREAR USUARIO \n3) SALIR \n -----> ")

    match resp1:
        case '1':

            encontrado = 0

            nombre_cliente = input("\nCUAL ES TU NOMBRE: ").upper()

            for cliente in Cliente.lstClientes:
                if cliente.nombre == nombre_cliente:
                    cliente_a = cliente
                    encontrado += 1
                    break
                else:
                    pass

            if encontrado == 1:
                os.system("cls")
                inicio()

            else:
                print("\nEL NOMBRE QUE INGRESASTE NO ES UN CLIENTE REGISTRADO, INTENTA DE NUEVO...")
                input("\nPRESS ENTER...")
                os.system("cls")

        case '2':
            os.system("cls")
            crear_cliente()

        case '3':
            print("\nHASTA LUEGO :D")
            i += 1

        case _:
            print("\nEL CARACTER QUE INGRESASTE ES INCORRECTO D:\n")
            input("\nPRESS ENTER...")
            os.system("cls")

