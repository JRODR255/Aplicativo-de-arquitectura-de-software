import tkinter as tk
from tkinter import messagebox, simpledialog

# Definición de la clase CajeroVista que maneja la interfaz gráfica
class CajeroVista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Cajero Automático")
        self.root.geometry("400x400")
        self.root.configure(bg="#22a4f3")
        self.root.protocol("WM_DELETE_WINDOW", self.finalizar_sesion)

        # Inicia mostrando el menú de inicio
        self.mostrar_menu_inicio()

    def mostrar_menu_inicio(self):
        # Limpia la pantalla
        self.limpiar_pantalla()

        # Crea una etiqueta de bienvenida
        inicio_label = tk.Label(self.root, text="Bienvenido al Cajero Automático", bg="#22a4f3", font=("Helvetica", 16))
        inicio_label.pack()

        # Crea etiquetas y campos de entrada para número de cuenta y PIN
        cuenta_label = tk.Label(self.root, text="Ingrese su número de cuenta (6 dígitos):", bg="#22a4f3")
        cuenta_label.pack()
        self.cuenta_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.cuenta_entry.pack()
        pin_label = tk.Label(self.root, text="Ingrese su PIN (4 dígitos numéricos):", bg="#22a4f3")
        pin_label.pack()
        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14))
        self.pin_entry.pack()

        # Crea un botón para iniciar sesión
        iniciar_button = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#ffdb58")
        iniciar_button.pack()

    def iniciar_sesion(self):
        # Obtiene el número de cuenta y el PIN ingresados
        numero_cuenta = self.cuenta_entry.get()
        pin = self.pin_entry.get()

        # Realiza validaciones en los datos ingresados
        if not numero_cuenta.isdigit() or len(numero_cuenta) != 6 or len(pin) != 4 or not pin.isdigit():
            # Muestra un mensaje de error si los datos son incorrectos
            messagebox.showerror("Error", "Número de cuenta o PIN incorrectos")
            return

        # Verifica el número de cuenta y el PIN en el controlador
        cuenta_index = self.controlador.verificar_pin(numero_cuenta, pin)

        if cuenta_index != -1:
            # Almacena el índice de la cuenta y muestra el menú principal
            self.cuenta_index = cuenta_index
            self.mostrar_menu_principal()
        else:
            # Muestra un mensaje de error si la verificación falla
            messagebox.showerror("Error", "Número de cuenta o PIN incorrectos")

    def mostrar_menu_principal(self):
        # Limpia la pantalla
        self.limpiar_pantalla()

        # Crea una etiqueta para el menú principal
        menu_label = tk.Label(self.root, text="Menú Principal", bg="#22a4f3", font=("Helvetica", 16))
        menu_label.pack()

        # Muestra el saldo de la cuenta
        saldo_label = tk.Label(self.root, text="Saldo: " + self.controlador.validar_saldo(self.cuenta_index), bg="#22a4f3")
        saldo_label.pack()

        # Crea botones para hacer retiros, congelar la cuenta y finalizar la sesión
        retirar_button = tk.Button(self.root, text="Hacer Retiro", command=self.solicitar_pin_retiro, bg="#ffdb58")
        retirar_button.pack()
        congelar_button = tk.Button(self.root, text="Congelar Cuenta", command=self.solicitar_pin_congelar, bg="#ffdb58")
        congelar_button.pack()
        salir_button = tk.Button(self.root, text="Finalizar Sesión", command=self.finalizar_sesion, bg="#ffdb58")
        salir_button.pack()

    def solicitar_pin_retiro(self):
        # Limpia la pantalla
        self.limpiar_pantalla()

        # Crea una etiqueta y campo de entrada para el PIN
        pin_label = tk.Label(self.root, text="Ingrese su PIN (4 dígitos numéricos):", bg="#22a4f3")
        pin_label.pack()
        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14))
        self.pin_entry.pack()

        # Crea un botón para confirmar el retiro
        confirmar_button = tk.Button(self.root, text="Confirmar", command=self.hacer_retiro, bg="#ffdb58")
        confirmar_button.pack()

    def solicitar_pin_congelar(self):
        # Limpia la pantalla
        self.limpiar_pantalla()

        # Crea una etiqueta y campo de entrada para el PIN
        pin_label = tk.Label(self.root, text="Ingrese su PIN (4 dígitos numéricos):", bg="#22a4f3")
        pin_label.pack()
        self.pin_entry = tk.Entry(self.root, show="*", font=("Helvetica", 14))
        self.pin_entry.pack()

        # Crea un botón para confirmar la congelación de la cuenta
        confirmar_button = tk.Button(self.root, text="Confirmar", command=self.congelar_cuenta, bg="#ffdb58")
        confirmar_button.pack()

    def hacer_retiro(self):
        # Obtiene el PIN ingresado
        pin = self.pin_entry.get()

        # Realiza validaciones en el PIN
        if len(pin) != 4 or not pin.isdigit() or not self.controlador.verificar_pin(self.cuenta_index, pin):
            # Muestra un mensaje de error si el PIN es incorrecto
            messagebox.showerror("Error", "PIN incorrecto")
            return

        # Limpia la pantalla
        self.limpiar_pantalla()

        # Solicita al usuario ingresar la cantidad a retirar
        cantidad_retiro = simpledialog.askfloat("Retiro", "Ingrese la cantidad a retirar:")
        if cantidad_retiro is None:
            self.mostrar_menu_principal()
            return

        if cantidad_retiro <= 0 or not self.controlador.hacer_retiro(self.cuenta_index, cantidad_retiro):
            # Muestra un mensaje de error si el retiro no es exitoso
            messagebox.showerror("Error", "No se pudo realizar el retiro.")
        else:
            # Muestra un mensaje de éxito y después el saldo actual
            self.limpiar_pantalla()
            mensaje_label = tk.Label(self.root, text="Estamos contando tu dinero...", bg="#22a4f3")
            mensaje_label.pack()
            self.root.after(2000, self.mostrar_saldo_actual)

    def congelar_cuenta(self):
        # Obtiene el PIN ingresado
        pin = self.pin_entry.get()

        # Realiza validaciones en el PIN
        if len(pin) != 4 or not pin.isdigit() or not self.controlador.verificar_pin(self.cuenta_index, pin):
            # Muestra un mensaje de error si el PIN es incorrecto
            messagebox.showerror("Error", "PIN incorrecto")
            return

        # Limpia la pantalla
        self.limpiar_pantalla()

        # Solicita al usuario la razón para congelar la cuenta
        razon_congelacion = simpledialog.askstring("Congelar Cuenta", "Razón para congelar la cuenta:")
        if razon_congelacion is None:
            self.mostrar_menu_principal()
            return

        # Llama al método del controlador para congelar la cuenta
        self.controlador.congelar_cuenta(self.cuenta_index, razon_congelacion)

        # Limpia la pantalla y muestra un mensaje de éxito
        self.limpiar_pantalla()
        mensaje_label = tk.Label(self.root, text="La cuenta ha sido congelada.", bg="#22a4f3")
        mensaje_label.pack()

    def finalizar_sesion(self):
        # Limpia la pantalla
        self.limpiar_pantalla()

        # Muestra un mensaje de despedida
        mensaje_label = tk.Label(self.root, text="Gracias por usar nuestros servicios.", bg="#22a4f3")
        mensaje_label.pack()

        # Después de 2 segundos, vuelve al menú de inicio
        self.root.after(2000, self.mostrar_menu_inicio)

    def mostrar_saldo_actual(self):
        # Obtiene el saldo actual de la cuenta
        saldo_actual = self.controlador.validar_saldo(self.cuenta_index)

        # Muestra el saldo y después finaliza la sesión
        saldo_label = tk.Label(self.root, text="Saldo actual: " + saldo_actual, bg="#22a4f3")
        saldo_label.pack()
        self.root.after(2000, self.finalizar_sesion)

    def limpiar_pantalla(self):
        # Limpia todos los elementos en la pantalla
        for widget in self.root.winfo_children():
            widget.destroy()

