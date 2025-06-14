import tkinter as tk
from tkinter import ttk, messagebox

class ArbolGenealogicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Genealógico Histórico")
        self.root.geometry("800x600")

        # Menú principal
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Exportar a Word")
        archivo_menu.add_command(label="Exportar a PDF")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        menu_bar.add_command(label="Árbol Completo", command=self.mostrar_arbol)
        menu_bar.add_command(label="Buscar", command=self.mostrar_busqueda)

        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Bienvenida
        self.mensaje_bienvenida()

    def mensaje_bienvenida(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        label = tk.Label(self.main_frame, text="Bienvenido al Árbol Genealógico de Familias Históricas de Chile", font=("Arial", 16), wraplength=700, justify="center")
        label.pack(pady=40)

    def mostrar_arbol(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        label = tk.Label(self.main_frame, text="Árbol genealógico completo (resumen)", font=("Arial", 14))
        label.pack(pady=20)

        arbol_ascii = '''
    ┌──────────────────────────────┐
    │     Familias Históricas     │
    └────────────┬────────────────┘
                │
     ┌──────────┴───────────┐
     │                      │
  Romero                 Hernández
     │                      │
  Valdés                 Sanfuentes
     │                      │
  Molina                   Parra
     │                      │
   Luco                   Coloma
     │                      │
  Silva                   Aguirre
     │                      │
   ↓                         ↓
 Descendencia histórica con aportes en:
 • Ejército Libertador
 • Iglesia Católica
 • Política y Constitución
 • Colonización y fundación de ciudades
        '''

        text = tk.Text(self.main_frame, wrap="word", font=("Courier", 10))
        text.insert("end", arbol_ascii)
        text.pack(expand=True, fill="both")

    def mostrar_busqueda(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        label = tk.Label(self.main_frame, text="Buscar por familia, siglo o nombre", font=("Arial", 14))
        label.pack(pady=20)

        frame = tk.Frame(self.main_frame)
        frame.pack()

        tk.Label(frame, text="Apellido o siglo:").grid(row=0, column=0, padx=5)
        entrada = tk.Entry(frame)
        entrada.grid(row=0, column=1, padx=5)

        def buscar():
            termino = entrada.get()
            messagebox.showinfo("Resultado", f"Buscar: {termino}\n(Aquí se mostrarán los resultados)")

        tk.Button(frame, text="Buscar", command=buscar).grid(row=0, column=2, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolGenealogicoApp(root)
    root.mainloop()
