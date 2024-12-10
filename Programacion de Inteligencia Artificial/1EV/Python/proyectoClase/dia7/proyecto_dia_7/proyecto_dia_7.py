class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre =  nombre
        self.apellidos = apellidos

class Cliente(Persona):
    def __init__(self, nombre, apellidos, n_cuenta, saldo):
        super().__init__(nombre, apellidos)
        self.n_cuenta = n_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nNº cuenta: {self.n_cuenta}\nSaldo: {self.saldo}\n"

    def depositar(self):
        print(f"Cliente: {self.nombre} {self.apellidos}\n")
        saldo_depositar = int(input("Cuánto dinero quieres depositar (€): "))
        self.saldo += saldo_depositar

    def retirar(self):
        print(f"Cliente: {self.nombre} {self.apellidos}\n")
        saldo_retirar = int(input("¿Cuánto dinero quieres retirar?"))
        self.saldo -= saldo_retirar

cliente1 = Cliente("Juan", "Fernandez", "ES6702410391118420591014", 20000)
cliente2 = Cliente("Paula", "Jiménez", "ES4114906219387844836624", 40000)

print(cliente1.__str__())
print(cliente2.__str__())

cliente1.depositar()
cliente1.retirar()

cliente2.depositar()
cliente2.retirar()

print(cliente1.__str__())
print(cliente2.__str__())