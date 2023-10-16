# Definición de la clase CuentaBancaria
class CuentaBancaria:
    # See ejecuta al crear una nueva instancia de la clase.
    def __init__(self, saldo_inicial, numero_cuenta, pin):
        # Inicia las propiedades de la cuenta con los valores proporcionados
        self.saldo = saldo_inicial
        self.numero_cuenta = numero_cuenta
        self.pin = pin
        self.congelada = False  # Indica si la cuenta está congelada o no
        self.razon_congelacion = ""  # Almacena la razón por la que la cuenta fue congelada (opcional)

    # Verifica si el PIN ingresado es el correcto
    def verificar_pin(self, pin):
        return self.pin == pin

    # Se muestra el saldo de la cuenta con formato monetario
    def obtener_saldo(self):
        return f"${self.saldo:,.2f}"

    # Permite realizar un retiro de la cuenta
    def hacer_retiro(self, cantidad):
        # Verifica si la cuenta no está congelada y si el saldo es suficiente para el retiro
        if not self.congelada and self.saldo >= cantidad:
            self.saldo -= cantidad  # Resta la cantidad del saldo
            return True  # Indica que el retiro fue exitoso
        return False  # Indica que el retiro no se pudo realizar

    # Método para congelar la cuenta (bloquearla) con una razón 
    def congelar_cuenta(self, razon=""):
        self.congelada = True  # Marca la cuenta como congelada
        self.razon_congelacion = razon  # Almacena la razón por la que se congeló la cuenta

    # Verifica si la cuenta está congelada
    def esta_congelada(self):
        return self.congelada

    # Obtiene el número de cuenta
    def obtener_numero_cuenta(self):
        return self.numero_cuenta

# Definición de la clase CajeroModelo
class CajeroModelo:
    # Constructor de la clase CajeroModelo, se ejecuta al crear una nueva instancia de la clase.
    def __init__(self):
        # Inicializa una lista de cuentas bancarias con valores iniciales ingresados dentro del programa de manera manual
        self.cuentas = [
            CuentaBancaria(saldo_inicial=12312315.0, numero_cuenta="123456", pin="1234"),
            CuentaBancaria(saldo_inicial=87127315.0, numero_cuenta="567890", pin="5678"),
            CuentaBancaria(saldo_inicial=574735.0, numero_cuenta="987654", pin="9876")
        ]

    # Método para obtener la lista de cuentas
    def obtener_cuentas(self):
        return self.cuentas
