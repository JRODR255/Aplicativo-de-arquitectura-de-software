# Importa las clases CajeroModelo y CajeroVista desde sus respectivos módulos
from modelo import CajeroModelo
from vista import CajeroVista

# Define la clase CajeroControlador, que actúa como el controlador en el patrón Modelo-Vista-Controlador (MVC)
class CajeroControlador:
    def __init__(self):
        # Inicia una instancia del modelo CajeroModelo
        self.modelo = CajeroModelo()

        # Inicia las variables para la vista y la cuenta seleccionada
        self.vista = None
        self.cuenta_seleccionada = None

    # Método para iniciar la aplicación
    def iniciar_aplicacion(self):
        # Crea una instancia de la vista CajeroVista, pasando self (el controlador) como argumento
        self.vista = CajeroVista(self)

        # Inicia el ciclo de eventos de la ventana
        self.vista.root.mainloop()

    # Método para verificar el PIN ingresado por el usuario
    def verificar_pin(self, numero_cuenta, pin):
        for i, cuenta in enumerate(self.modelo.cuentas):
            if cuenta.numero_cuenta == numero_cuenta and cuenta.verificar_pin(pin):
                # Si se encuentra una coincidencia, devuelve el índice de la cuenta
                return i
        # Si no se encuentra ninguna coincidencia, devuelve -1
        return -1

    # Método para obtener y validar el saldo de una cuenta
    def validar_saldo(self, cuenta_index):
        return self.modelo.cuentas[cuenta_index].obtener_saldo()

    # Método para realizar un retiro de una cuenta
    def hacer_retiro(self, cuenta_index, cantidad):
        return self.modelo.cuentas[cuenta_index].hacer_retiro(cantidad)

    # Método para congelar una cuenta con una razón opcional
    def congelar_cuenta(self, cuenta_index, razon_congelacion=""):
        self.modelo.cuentas[cuenta_index].congelar_cuenta(razon_congelacion)

# Bloque principal que se ejecuta si este script se ejecuta directamente
if __name__ == "__main__":
    # Crea una instancia de la clase CajeroControlador
    controlador = CajeroControlador()

    # Inicia la aplicación llamando al método iniciar_aplicacion
    controlador.iniciar_aplicacion()
