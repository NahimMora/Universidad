import tkinter as tk
from tkinter import messagebox
import math
from metodos import biseccion, regula_falsi, newton, secante

def abrir_menu():
    # Función a evaluar
    f = lambda x: math.e**x - x**2 + 1

    # Ventana principal
    root = tk.Tk()
    root.title("Comparador de Métodos Numéricos")
    root.geometry("450x350")

    # Diccionario de métodos
    metodos = {
        "Bisección": biseccion,
        "Regula Falsi": regula_falsi,
        "Newton": newton,
        "Secante": secante
    }

    # Lista de métodos seleccionados
    seleccionados = []

    # Función para actualizar selección
    def toggle_metodo(metodo):
        if metodo in seleccionados:
            seleccionados.remove(metodo)
        else:
            seleccionados.append(metodo)
        label_seleccion.config(text="Métodos seleccionados: " + ", ".join(seleccionados))

    # Botones para cada método
    for metodo in metodos.keys():
        btn = tk.Button(root, text=metodo, width=15, command=lambda m=metodo: toggle_metodo(m))
        btn.pack(pady=5)

    # Etiqueta que muestra los métodos seleccionados
    label_seleccion = tk.Label(root, text="Métodos seleccionados: ")
    label_seleccion.pack(pady=10)

    # Entradas para los valores a y b
    tk.Label(root, text="Valor inicial a:").pack()
    entry_a = tk.Entry(root)
    entry_a.pack()

    tk.Label(root, text="Valor inicial b:").pack()
    entry_b = tk.Entry(root)
    entry_b.pack()

    # Función para ejecutar métodos
    def ejecutar():
        if not seleccionados:
            messagebox.showwarning("Atención", "Selecciona al menos un método")
            return

        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")
            return

        resultados = ""
        for metodo in seleccionados:
            func = metodos[metodo]

            try:
                if metodo == "Newton":
                    x0 = a  # Usamos 'a' como inicial
                    resultado = func(f, x0)
                elif metodo == "Secante":
                    resultado = func(f, a, b)
                else:
                    resultado = func(f, a, b)

                if resultado is None:
                    resultados += f"{metodo}: No se puede calcular la raíz en este intervalo.\n"
                else:
                    raiz, iteraciones = resultado
                    resultados += f"{metodo}: Raíz ≈ {raiz:.6f}, Iteraciones = {iteraciones}\n"
            except Exception as e:
                resultados += f"{metodo}: Error al calcular ({e})\n"

        messagebox.showinfo("Resultados", resultados)

    # Botón para ejecutar
    btn_ejecutar = tk.Button(root, text="Calcular Raíces", command=ejecutar, bg="lightgreen")
    btn_ejecutar.pack(pady=15)

    root.mainloop()
